const { ipcRenderer } = require('electron');

const dropArea = document.getElementById('drop-area');

// Add event listeners for drag events
dropArea.addEventListener('dragenter', (event) => {
    event.preventDefault();
    dropArea.classList.add('hover');
    // Send message to main process to increase window size and make it topmost
    ipcRenderer.send('resize-window', 800, 600);  // Example: Increase to 800x600
    ipcRenderer.send('set-topmost', true);  // Make the window topmost
});

dropArea.addEventListener('dragover', (event) => {
    event.preventDefault();
});

dropArea.addEventListener('dragleave', () => {
    dropArea.classList.remove('hover');
    // Restore window size after drag leaves
    ipcRenderer.send('resize-window', 600, 400);  // Example: Restore to 600x400
    ipcRenderer.send('set-topmost', false);  // Remove topmost
});

dropArea.addEventListener('drop', (event) => {
    event.preventDefault();
    dropArea.classList.remove('hover');
    // Get the file from the drop event (optional)
    const files = event.dataTransfer.files;
    if (files.length > 0) {
        console.log('File dropped:', files[0].path);
    }
    // Optionally, you can resize the window again after drop and remove topmost status
    ipcRenderer.send('resize-window', 600, 400);  // Restore size after file drop
    ipcRenderer.send('set-topmost', false);  // Remove topmost after drop
});
