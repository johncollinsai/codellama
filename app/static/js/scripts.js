document.addEventListener('DOMContentLoaded', function () {
    const promptForm = document.getElementById('prompt-form');
    const resultElement = document.getElementById('result');
    const skeletonScreen = document.getElementById('skeleton-screen');
    const spinner = document.querySelector('.spinner');
    const submitButton = document.querySelector('.circle-btn');
    const promptTextArea = document.getElementById('prompt');
    let modality;

    function updateSubmitButtonColor() {
        if (promptTextArea.value.trim() !== '') {
            submitButton.style.backgroundColor = '#6f42c1';
        } else {
            submitButton.style.backgroundColor = '#b3b3b3';
        }
    }

    updateSubmitButtonColor();

    promptTextArea.addEventListener('input', updateSubmitButtonColor);
    promptTextArea.addEventListener('keydown', function(event) {
        if (event.key === 'Enter') {
            event.preventDefault(); // prevent the new line from being added
            promptForm.dispatchEvent(new Event('submit')); // submit the form
        }
    });

    function displayResult(result) {
        resultElement.innerHTML = result;
    }

    function displayError(error, element) {
        element.innerHTML = `<div class="alert alert-danger" role="alert">${error}</div>`;
    }

    function toggleSpinner(visible) {
        spinner.style.display = visible ? 'flex' : 'none';
        skeletonScreen.classList.toggle('d-none', !visible);
    }

    function fetchWithTimeout(resource, options, timeout = 60000) {
        return Promise.race([
            fetch(resource, options),
            new Promise((_, reject) =>
                setTimeout(() => reject(new Error("Request timed out")), timeout)
            ),
        ]);
    }

    async function fetchData(prompt, modality) {
        const formData = new FormData(promptForm);
        formData.append("modality", modality);

        try {
            const response = await fetchWithTimeout("/get_completion", {
                method: "POST",
                body: formData,
            }, 180000);

            if (response.ok) {
                const data = await response.json();
                console.log("Data received: " + JSON.stringify(data));
                return data;
            } else {
                console.error("Error occurred while fetching data", response.statusText);
                return { success: false, error: "An error occurred while fetching data. Please try again later." };
            }
        } catch (error) {
            console.error("Error occurred while fetching data", error);
            return {
                success: false,
                error: "An error occurred while fetching data. Please try again later.",
            };
        }
    }

    async function handleFormSubmit(event) {
        event.preventDefault();
        toggleSpinner(true);

        const prompt = promptForm.elements["prompt"].value;

        try {
            const result = await fetchData(prompt, modality);

            if (result.success) {
                displayResult(`<h3>Model: ${modality}</h3><h5 class="text-lightgrey">Company: ${prompt}</h5><pre class="text-white">${result.response}</pre>`);
            } else {
                displayError(result.error, resultElement);
            }
        } catch (error) {
            displayError("An error occurred while processing the request. Please try again later.", resultElement);
        }

        toggleSpinner(false);
    }

    const modalityButtons = document.querySelectorAll('.chat-menu button');

    modalityButtons.forEach(button => {
        button.addEventListener('click', () => {
            modality = button.dataset.value;
        });
    });

    promptForm.addEventListener('submit', handleFormSubmit);
});
