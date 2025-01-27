const { app, BrowserWindow, ipcMain } = require('electron');
const fs = require('fs');
const { exec } = require('child_process');

let window;

function createWindow() {
    try {
        let windowSettings = loadWindowSettings();
        if (!windowSettings) {
            windowSettings = { width: 800, height: 600, x: 100, y: 100, resizable: false, movable: false, frame: false };
        }

        window = new BrowserWindow({
            width: windowSettings.width,
            height: windowSettings.height,
            x: windowSettings.x,
            y: windowSettings.y,
            resizable: windowSettings.resizable,
            movable: windowSettings.movable,
            frame: windowSettings.frame,
            webPreferences: {
                nodeIntegration: true,
                contextIsolation: false
            }
        });

        window.loadFile('index.html');

        ipcMain.on('resize-window', (event, width, height) => {
            window.setSize(width, height);
        });

        ipcMain.on('set-topmost', (event, isTopmost) => {
            window.setAlwaysOnTop(isTopmost);
        });
    } catch (error) {
        // Send error to logger.py
        exec(`python logger.py "${error.message}"`, (err, stdout, stderr) => {
            if (err) {
                console.error(`Error logging failed: ${stderr}`);
            }
        });
    }
}

app.on('ready', createWindow);
app.on('window-all-closed', () => {
    if (process.platform !== 'darwin') {
        app.quit();
    }
});