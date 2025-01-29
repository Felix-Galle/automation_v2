const { ipcRenderer } = require('electron');

const dropArea = document.getElementById('drop-area');

dropArea.addEventListener('dragenter', (event) => {
    event.preventDefault();
    dropArea.classList.add('hover');
    ipcRenderer.send('resize-window', 800, 600);
    ipcRenderer.send('set-topmost', true);
});

dropArea.addEventListener('dragover', (event) => {
    event.preventDefault();
});

dropArea.addEventListener('dragleave', () => {
    dropArea.classList.remove('hover');
    ipcRenderer.send('resize-window', 600, 400);
    ipcRenderer.send('set-topmost', false);
});

dropArea.addEventListener('drop', (event) => {
    event.preventDefault();
    dropArea.classList.remove('hover');
    const files = event.dataTransfer.files;
    if (files.length > 0) {
        console.log('File dropped:', files[0].path);
    }
    ipcRenderer.send('resize-window', 600, 400);
    ipcRenderer.send('set-topmost', false);
});
