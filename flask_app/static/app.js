// Activer le mode nuit par défaut
document.addEventListener('DOMContentLoaded', function() {
    const toggleSwitch = document.getElementById('toggleDarkMode');
    toggleSwitch.checked = true;  // Coche la case pour le mode nuit par défaut
    document.body.classList.add('dark-mode');  // Ajoute la classe dark-mode au corps de la page

    // Afficher l'icône appropriée
    document.querySelector('.sun').style.display = 'inline';  // Affiche l'icône du soleil
    document.querySelector('.moon').style.display = 'none';   // Cache l'icône de la lune
});

document.getElementById('toggleDarkMode').addEventListener('change', function() {
    document.body.classList.toggle('dark-mode');

    // Inverser l'affichage des icônes
    let sunIcon = document.querySelector('.sun');
    let moonIcon = document.querySelector('.moon');

    if (document.body.classList.contains('dark-mode')) {
        sunIcon.style.display = 'inline';
        moonIcon.style.display = 'none';
    } else {
        sunIcon.style.display = 'none';
        moonIcon.style.display = 'inline';
    }
});

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
};