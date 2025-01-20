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
        x: 500,             // x pos
        y: 400,             // y pos
        resizable: false,    // Prevent resizing
        movable: false,      // Prevent moving (note: this is not a direct property)
        frame: false,        // Remove window frame (no close/minimize/maximize buttons)
        webPreferences: {
            nodeIntegration: true, // Enable Node.js integration
            contextIsolation: false // Disable context isolation for easier access to Node.js
        }
    });
    
    window.loadFile('index.html');

    // Enable drag-and-drop functionality
    window.webContents.on('will-navigate', (event) => {
        event.preventDefault();
    });

    window.webContents.on('did-finish-load', () => {
        window.webContents.executeJavaScript(`
            const dropArea = document.getElementById('drop-area');
            dropArea.addEventListener('dragover', (event) => {
                event.preventDefault();
                dropArea.classList.add('highlight');
            });

            dropArea.addEventListener('dragleave', () => {
                dropArea.classList.remove('highlight');
            });

            dropArea.addEventListener('drop', (event) => {
                event.preventDefault();
                dropArea.classList.remove('highlight');
                const files = event.dataTransfer.files;
                if (files.length > 0) {
                    const filePath = files[0].path;
                    // Send the file path to the Python script
                    window.webContents.send('file-dropped', filePath);
                }
            });
        `);
    });

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

// IPC listener for file dropped event
ipcMain.on('file-dropped', (event, filePath) => {
    console.log('File dropped:', filePath);
    handleFileTransfer(filePath);
});

app.on('ready', createWindow);

app.on('window-all-closed', () => {
    if (process.platform !== 'darwin') {
        app.quit();
    }
});