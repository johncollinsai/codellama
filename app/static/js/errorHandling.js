// errorHandling.js
function logError(message, error) {
    console.error(`Error: ${message}`, error);
}

function logInfo(message) {
    console.log(`Info: ${message}`);
}

function logWarning(message) {
    console.warn(`Warning: ${message}`);
}

function displayError(message, errorElement) {
    errorElement.innerHTML = `<h3 class="text-danger">Error</h3><p class="text-danger">${message}</p>`;
}
