
document.addEventListener("DOMContentLoaded", loadGitHubCalendar);

async function loadGitHubCalendar() {
    const calendar = document.getElementById("contributions-calendar");
    const countElement = document.getElementById("contributions-count");
    const statusElement = document.getElementById("github-status");

    try {
        const response = await fetch("data/github-contributions.json", {
            cache: "no-store"
        });

        if (!response.ok) {
            throw new Error(`Error HTTP: ${response.status}`);
        }

        const data = await response.json();

        if (!Array.isArray(data.weeks)) {
            throw new Error("El JSON no contiene un calendario válido.");
        }

        renderCalendar(data, calendar);

        countElement.textContent =
            `${data.totalContributions.toLocaleString("es-ES")} contribuciones en los últimos 12 meses`;

        statusElement.textContent = data.generatedAt
            ? `Última actualización: ${new Date(data.generatedAt).toLocaleDateString("es-ES")}`
            : "Contribuciones cargadas correctamente.";

    } catch (error) {
        console.error("Error al cargar el calendario de GitHub:", error);

        countElement.textContent = "No se pudieron cargar las contribuciones.";
        statusElement.textContent = "Error al conectar con los datos de GitHub.";
    }
}

function renderCalendar(data, calendar) {
    calendar.innerHTML = "";

    data.weeks.forEach(week => {
        week.contributionDays.forEach(day => {
            const cell = document.createElement("div");
            const level = getContributionLevel(day.contributionCount);

            cell.classList.add("contribution-day", `level-${level}`);

            cell.title =
                `${day.contributionCount} contribuciones el ${formatDate(day.date)}`;

            cell.setAttribute(
                "aria-label",
                `${day.contributionCount} contribuciones el ${formatDate(day.date)}`
            );

            calendar.appendChild(cell);
        });
    });
}

function getContributionLevel(count) {
    if (count === 0) return 0;
    if (count <= 3) return 1;
    if (count <= 6) return 2;
    if (count <= 9) return 3;

    return 4;
}

function formatDate(date) {
    return new Date(`${date}T12:00:00`).toLocaleDateString("es-ES", {
        day: "numeric",
        month: "long",
        year: "numeric"
    });
}
