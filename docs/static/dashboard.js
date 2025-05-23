// response is json file
const API_URL = 'https://attendance-api-lw-906041588659.europe-west10.run.app/me';

function updateMetric(id, value) {
  const element = document.getElementById(id);
  element.textContent = `${value}%`;

  // reset previous styles
  element.classList.remove('low-score');

  // apply red color if value is less than 65%
  if (value < 65) {
    element.classList.add('low-score');
  }
}

function updateMetricAbsent(id, value) {
  const element = document.getElementById(id);
  element.textContent = `${value}%`;

  // reset previous styles
  element.classList.remove('low-score');

  // apply red color if value is less than 65%
  if (value >= 0.1) {
    element.classList.add('low-score');
  }
}


    



async function fetchDashboardData() {
  try {
    const response = await fetch(API_URL,
      {
        method: 'GET',
        credentials: 'include'  // this is important!
      }
    );
    const data = await response.json();


    const numericAttendance = parseFloat(data.attendance[0].Absenteismo);
    updateMetricAbsent('attendanceValue', numericAttendance);
    const numericRate = parseFloat(data.general[0].rate.replace('%', ''));
    updateMetric('exerciseValue', numericRate);

    // layout page with user data
    const user_login = data.user_login || "User Login";
    const name = data.user_name || "Guest";
    const avatar = data.avatar || "static/null-person.png";

    document.getElementById("thank-you-title").textContent = `Welcome, ${name}!`;
    document.getElementById("avatar").src = avatar;



  } catch (error) {
    console.error('Failed to fetch dashboard data:', error);
    document.getElementById('attendanceValue').textContent = 'Error';
    document.getElementById('exerciseValue').textContent = 'Error';

    updateMetric('attendanceValue', 70); // data.attendance);
    const numericRate = parseFloat(data.general[0].rate.replace('%', ''));
    updateMetric('exerciseValue', numericRate);
  }
}

fetchDashboardData();