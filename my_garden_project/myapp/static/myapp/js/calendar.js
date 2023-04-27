const currentYear = new Date().getFullYear();
console.log('currentYear', currentYear)
  const daysInMonth = {
    january: 31,
    february: 28,
    march: 31,
    april: 30,
    may: 31,
    june: 30,
    july: 31,
    august: 31,
    september: 30,
    october: 31,
    november: 30,
    december: 31,
  };
  gardenCalendar();

//creation du calendrier perpétuel
  function gardenCalendar() {
    //pour chaque mois un id
    for (const month in daysInMonth) {
      const daysContainer = document.getElementById(`${month}-days`);

      //pour chaque jour creer une div
      for (let i = 1; i <= daysInMonth[month]; i++) {
        const dayElement = document.createElement("div");
        //ajout de la class day a cette div
        dayElement.className = "day";
        //et de la val de i
        dayElement.innerText = i;
        //faire apparaitre ces div dans le dom
        daysContainer.appendChild(dayElement);
      }
    }
  }


//l'année n'est pas prise en compte
//La méthode padStart() permet de compléter la chaîne courante avec une chaîne de caractères donnée afin d'obtenir une chaîne de longueur fixée, 2 dans ce cas
function formatDateWithoutYear(date) {
  const month = String(date.getMonth() + 1).padStart(2, '0');
  const day = String(date.getDate()).padStart(2, '0');
  return `${month}-${day}`;
}


const updatePlanningBtns = document.querySelectorAll('.update-planning');
console.log('updatePlanningBtns:', updatePlanningBtns);

for (let i = 0; i < updatePlanningBtns.length; i++) {
  const updatePlanningBtn = updatePlanningBtns[i];
  console.log('updatePlanningBtn:', updatePlanningBtn);
  updatePlanningBtn.addEventListener('click', () => {
    let productId = updatePlanningBtn.dataset.product;

    // Retire la classe 'active-btn' des autres boutons
    updatePlanningBtns.forEach((btn) => {
      btn.classList.remove('active-btn');
    });

    // Ajoute la classe 'active-btn' au bouton cliqué
    updatePlanningBtn.classList.add('active-btn');
    updateCalendar(productId);
  });
}

function updateCalendar(productId) {
  console.log('Appel de updateCalendar pour le produit', productId);

  const url = '/myapp/update_calendar/';
  fetch(url, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'X-CSRFToken': csrftoken,
    },
    body: JSON.stringify({ productId }),
  })
    .then(response => response.json())
    .then(data => {
      console.log('data de update calendar', data);
      displayEvents(data.events);


    })
    .catch(error => console.log('Error:', error));

}


function displayEvents(events) {
  // Effacer les anciens événements
  const previousEvents = document.querySelectorAll('.event-container');
  previousEvents.forEach((event) => event.remove());

  // Intègration des div relative a l event
  for (const month in daysInMonth) {
    for (let i = 1; i <= daysInMonth[month]; i++) {
      const currentDate = new Date(`${currentYear}-${month}-${i}`);
      const currentDateWithoutYear = formatDateWithoutYear(currentDate);

      const daysContainer = document.getElementById(`${month}-days`);
      const dayElement = daysContainer.querySelector(`.day:nth-child(${i})`);

      events.forEach((event) => {
        const startDate = new Date(event.startDate);
        const endDate = new Date(event.endDate);
        const startDateWithoutYear = formatDateWithoutYear(startDate);
        const endDateWithoutYear = formatDateWithoutYear(endDate);

        const eventDurationInDays = (endDate - startDate) / (1000 * 60 * 60 * 24);
        let displayEvent = false;

        for (let j = 0; j <= eventDurationInDays; j++) {
          const eventDate = new Date(startDate);
          eventDate.setDate(startDate.getDate() + j);
          const eventDateWithoutYear = formatDateWithoutYear(eventDate);

          if (currentDateWithoutYear === eventDateWithoutYear) {
            displayEvent = true;
            break;
          }
        }

        if (displayEvent) {
          const eventElement = document.createElement('div');
          eventElement.className = `event-container event ${event.name}`;
          dayElement.appendChild(eventElement);
         // console.log('eventElement', eventElement);
        }

        //fltrage des events

          const itemEvents = document.querySelectorAll('.item-event');
          itemEvents.forEach(itemEvent => {
          itemEvent.addEventListener('click', () => {
         // console.log(itemEvent)
          // Récupération du produit sélectionné et de l'événement

          const selectedEventName = itemEvent.textContent.trim();
         // console.log('selectedEventName', selectedEventName)

          // Cachez tous les events elements qui ne correspondent pas a l evenement
          const eventElements = document.querySelectorAll('.event-container');
         // console.log(eventElements)
          eventElements.forEach(eventElement => {
             if (eventElement.classList.contains(selectedEventName)) {
                    eventElement.style.display = 'block';
             } else {
                    eventElement.style.display = 'none';
                  }
                });
              });
            });
            });
            }
            }
    }





//fltrage des events

const itemEvents = document.querySelectorAll('.item-event');
itemEvents.forEach(itemEvent => {
  itemEvent.addEventListener('click', () => {
 // console.log(itemEvent)
    // Récupération du produit sélectionné et de l'événement

    const selectedEventName = itemEvent.textContent.trim();
    //console.log('selectedEventName', selectedEventName)

      // Cachez tous les events elements qui ne correspondent pas a l evenement
    const eventElements = document.querySelectorAll('.event-container');
   // console.log(eventElements)
    eventElements.forEach(eventElement => {
      if (eventElement.classList.contains(selectedEventName)) {
        eventElement.style.display = 'block';
      } else {
        eventElement.style.display = 'none';
      }
    });
  });
});



//maj de l'affichage des dates dans la partie responsive pour n'afficher que le jour et mois
// éléments `.data-item`.
function updateDateItems() {
  // éléments `.data-item`.
  const dataItems = document.querySelectorAll(".data-item");

  dataItems.forEach(dataItem => {
    // Récupère la chaîne de date.
    const dateString = dataItem.textContent;

    // parties de la date.
    const dateParts = dateString.split(' ');
    const year = dateParts[2];
    const month = dateParts[1];
    const day = dateParts[0];

    // nouvelle chaîne de date dans l'élément data-ite
    dataItem.textContent =  day + " " + month ;
  });
}

updateDateItems();








