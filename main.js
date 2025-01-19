const { app, BrowserWindow, ipcMain } = require('electron');
const { spawn } = require('child_process');

let window;
let python;

// Create the main window
function createWindow() {
    window = new BrowserWindow({ width: 800, height: 600 });
    window.loadFile('index.html');

    // Start the Python script
    python = spawn('python', ['./msg.py']);
    
    // Listen for messages from the Python script
    python.stdout.on('data', function(data) {
        const message = data.toString('utf8').trim();
        if (message) {
            window.webContents.send('receive-message', message); // Send the message to the renderer process
        }
    });

    python.stderr.on('data', (data) => {
        console.error(`stderr: ${data}`);
    });

    python.on('close', (code) => {
        console.log(`Python process exited with code ${code}`);
    });
}

// Handle sending messages from the renderer process
ipcMain.on('send-message', (event, message, targetIp) => {
    const target = targetIp ? targetIp : '255.255.255.255'; // Use broadcast if no IP is provided
    python.stdin.write(`${message}\n${target}\n`); // Send message and target IP to Python script
});

app.on('ready', createWindow);

app.on('window-all-closed', () => {
    if (process.platform !== 'darwin') {
        app.quit();
    }
});