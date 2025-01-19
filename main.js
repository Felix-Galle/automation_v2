const { app, BrowserWindow, ipcMain } = require('electron');
const { spawn } = require('child_process');

let window;
let python;

// Create the main window
function createWindow() {
    window = new BrowserWindow({ width: 800, height: 600 });
    window.loadFile('index.html');

    // Start the Python script for PC discovery
    python = spawn('python', ['./pc_info.py']);
    
    // Listen for broadcasting PCs from the Python script
    python.stdout.on('data', function(data) {
        try {
            const pcs = JSON.parse(data.toString('utf8').trim());
            if (Array.isArray(pcs)) {
                window.webContents.send('update-pcs', pcs); // Send the list of PCs to the renderer process
            }
        } catch (error) {
            console.error('Error parsing PC data:', error);
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