// Don't delete any files from the external JS files
// Function to save or send data
async function processData(data, id) {
  let dataList = [];

  // Check if data already exists in local storage
  const existingData = localStorage.getItem('userData');
  if (existingData) {
    dataList = JSON.parse(existingData);
  }

  // Add new data to the list
  dataList.unshift(`${id}: ${data}`);

  // Check if user is online
  if (navigator.onLine) {
    // Send data to server
    try {
      const response = await fetch('https://mrlwitwma1.pythonanywhere.com/data', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(dataList)
      });
      // Clear local storage after successfully sending data
      localStorage.removeItem('userData');
    } catch (error) {
      console.error('Error sending data:', error);
    }
  } else {
    // Store data locally
    localStorage.setItem('userData', JSON.stringify(dataList));
  }
}