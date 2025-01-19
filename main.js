const { app, BrowserWindow, ipcMain } = require('electron');
const { spawn } = require('child_process');

let window;
let python_pc_info;
let python_msg;

// Create the main window
function createWindow() {
    window = new BrowserWindow({ 
        width: 100,          // Fixed width
        height: 75,         // Fixed height
        x: 100,             // x pos
        y: 100,             //y pos
        resizable: false,    // Prevent resizing
        movable: false,      // Prevent moving (note: this is not a direct property)
        frame: false,        // Remove window frame (no close/minimize/maximize buttons)
        webPreferences: {
            nodeIntegration: true, // Enable Node.js integration
            contextIsolation: false // Disable context isolation for easier access to Node.js
        }
    });
    
    window.loadFile('index.html');

    // Start the Python script for PC discovery
    python_pc_info = spawn('python', ['./pc_info.py']);
    
    // Listen for broadcasting PCs from the Python script
    python_pc_info.stdout.on('data', function(data) {
        try {
            const pcs = JSON.parse(data.toString('utf8').trim());
            if (Array.isArray(pcs)) {
                window.webContents.send('update-pcs', pcs); // Send the list of PCs to the renderer process
            }
        } catch (error) {
            console.error('Error parsing PC data:', error);
        }
    });

    python_pc_info.stderr.on('data', (data) => {
        console.error(`stderr: ${data}`);
    });

    python_pc_info.on('close', (code) => {
        console.log(`Python process exited with code ${code}`);
    });
}

app.on('ready', createWindow);

app.on('window-all-closed', () => {
    if (process.platform !== 'darwin') {
        app.quit();
    }
});