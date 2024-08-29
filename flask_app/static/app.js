document.getElementById('predictionForm').onsubmit = function(e) {
    e.preventDefault();
    let text = document.getElementById('text').value;
    
    if (!text.trim()) {
        alert('Please enter some text.');
        return;
    }

    fetch('/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        body: 'text=' + encodeURIComponent(text)
    })
    .then(response => response.json())
    .then(data => {
        let resultDiv = document.getElementById('result');
        if (data.error) {
            resultDiv.innerHTML = `<div class="alert alert-danger">${data.error}</div>`;
        } else {
            let tags = data.predicted_tags.map(tag => `<span class="badge bg-primary">${tag}</span>`).join(' ');
            resultDiv.innerHTML = `
                <h3>Predicted Tags:</h3>
                <p>${tags}</p>
            `;
        }
    })
    .catch(error => {
        console.error('Error:', error);
        document.getElementById('result').innerHTML = '<div class="alert alert-danger">An error occurred while processing your request.</div>';
    });
}