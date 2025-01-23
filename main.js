const { app, BrowserWindow, ipcMain } = require('electron');
const fs = require('fs');

// Global window variable
let window;

// Function to load window settings from JSON file
function loadWindowSettings() {
    const settingsPath = 'settings/win_dim_settings.json';
    if (!fs.existsSync(settingsPath)) {
        console.log(`Error: The settings filepath '${settingsPath}' does not exist.`);
        return null;
    }

    try {
        const data = fs.readFileSync(settingsPath, 'utf8');
        const settings = JSON.parse(data);
        console.log(`Loaded window dimensions: ${settings}`);
        return settings.window_position || null;
    } catch (error) {
        console.error('Error reading the settings file:', error);
        return null;
    }
}

// Create the main window
function createWindow() {
    let windowSettings = loadWindowSettings();  // Load settings from JSON

    if (!windowSettings) {
        // Default settings if no settings found
        windowSettings = { width: 800, height: 600, x: 100, y: 100, resizable: false, movable: false, frame: false };
    }

    // Create the Electron window with settings
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

    // Additional window setup...
}

app.on('ready', createWindow);

app.on('window-all-closed', () => {
    if (process.platform !== 'darwin') {
        app.quit();
    }
});