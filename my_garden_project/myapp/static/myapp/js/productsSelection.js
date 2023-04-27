

// récupère tous les boutons avec la classe "update-selection"
const updateBtns = document.querySelectorAll('.update-selection');

// Pour chaque bouton updateBtn trouvé, on ajoute un écouteur d'événements "click"
for (let i = 0; i < updateBtns.length; i++) {
  const updateBtn = updateBtns[i]  ;
  console.log('Update btn:', updateBtn);

  updateBtn.addEventListener('click', () => {
    // récupère l'ID du produit associé à ce bouton
    let productId = updateBtn.dataset.product;
    // On récupère l'action à effectuer (ajouter ou supp le produit de la sélection)
    const action = updateBtn.dataset.action;
    console.log('productId:', productId, 'action:', action);

    // On vérifie si l'utilisateur est connecté
    console.log('user:', user);
    if (user === 'AnonymousUser') {
      console.log('Not logged in');
    } else {
      // Si l'utilisateur est connecté, on appelle la fonction updateSelection avec les paramètres "productId", 'action" et fonction displayModal qui renvoie le message
      updateSelection(productId, action, displayModal);

    }
  });
}

// Envoie une requête back pour maj la sélection d'un utilisateur
function updateSelection(productId, action, displayModal) {
  //console.log('User logged in, sending data');

  const url = '/myapp/update_selection/';

  fetch(url, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'X-CSRFToken': csrftoken,
    },
    body: JSON.stringify({ productId, action }),
  })
    .then(response => response.json())
    .then(data => {

      // Une fois que la requête est terminée, on récupère la partie HTML
      // de la sélection de l'utilisateur et on la met à jour
      if (data.success && data.action === 'add') {
        displayModal(data.message);

      } else if (data.success && data.action === 'remove') {




        console.log('messageRemove:', data.message, 'action:', data.action);
        displayModal(data.message);
        const selectionDiv = document.querySelector('.selection');
        selectionDiv.innerHTML = data.html;

        updateDateItems();

        console.log('productId removed:', productId, 'action:', action);

        // Réassigner les boutons update-selection
        const updateBtns = document.querySelectorAll('.update-selection');
        for (let i = 0; i < updateBtns.length; i++) {
          const updateBtn = updateBtns[i];
          console.log('Update btn resigned:', updateBtn);

          updateBtn.addEventListener('click', () => {
            // récupère l'ID du produit associé à ce bouton
            let productId = updateBtn.dataset.product;
            // On récupère l'action à effectuer (ajouter ou supp le produit de la sélection)
            const action = updateBtn.dataset.action;


            // On vérifie si l'utilisateur est connecté
            console.log('user:', user);
            if (user === 'AnonymousUser') {
              console.log('Not logged in');
            } else {
              // Si l'utilisateur est connecté, on rappelle la fonction updateSelection avec les paramètres "productId", 'action" et fonction displayModal qui renvoie le message
              updateSelection(productId, action, displayModal);

            }
          });
        }
      }
    })
}



// Affichage modal
function displayModal(message) {
  const modal = document.querySelector('.add-message');
 // console.log(modal);
  const text = modal.querySelector('.message');

  if (message) {
    text.innerHTML = message;
    modal.classList.add('active');
    setTimeout(() => {
      modal.classList.remove('active');
    }, 3500);
  }
}

const infoBtns = document.querySelectorAll('.info-modal');
const infoModalContents = document.querySelectorAll('.info-modal-content');

for (let i = 0; i < infoBtns.length; i++) {
  infoBtns[i].addEventListener("mouseover", () => {
    infoModalContents[i].style.display = 'block';
  });

  infoBtns[i].addEventListener("mouseout", () => {
    infoModalContents[i].style.display = 'none';
  });
}



