document.addEventListener("DOMContentLoaded", function() {
    const ctx = document.getElementById('GraficaTec').getContext('2d');
    const datosX = tecnologias;
    const datosY = cantidades;

    const miGrafica = new Chart(ctx, {
        type: 'line',
        data: {
            labels: datosX,
            datasets: [{
                label: 'Tecnologías más solicitadas',
                data: datosY,
                borderColor: 'rgba(75, 192, 192, 1)',
                backgroundColor: 'rgba(75, 192, 192, 0.2)',
                borderWidth: 2,
                tension: 0.3
            }]
        },
        options: {
            responsive: true,
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
});