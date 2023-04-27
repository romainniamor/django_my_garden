
  // récupère tous les boutons avec la classe update-collection
  const addBtns = document.querySelectorAll('.update-collection');

  // Pour chaque bouton de addBtns trouvé, on ajoute un écouteur d'événements "click"
  for (let i = 0; i < addBtns.length; i++) {
    const addBtn = addBtns[i];
    console.log('Add btn:', addBtn);

    addBtn.addEventListener('click', () => {
      // récupère l'ID de la carte conseil associé à ce bouton
      let trickId = addBtn.dataset.trick;
      // On récupère l'action à effectuer (ajouter ou supp l element de la selection)
      const action = addBtn.dataset.action;
      console.log('trickId:', trickId, 'action:', action, 'user:', user);
      updateCollection(trickId, action, displayModal);
    });
  };


// Envoie une requête back pour maj la sélection d'un utilisateur
function updateCollection(trickId, action, displayModal) {
  console.log('lancement de la fonction updateCollection');
  const url = '/myapp/update_collection/';
  fetch(url, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'X-CSRFToken': csrftoken,
    },
    body: JSON.stringify({ trickId, action }),
  })
    .then(response => response.json())
    .then(data => {
      // Ajoutez cette condition
      if (data.success && data.action === 'add') {
        displayModal(data.message);

      } else if (data.success && data.action === 'remove') {
        console.log('messageRemove:', data.message, 'action:', data.action);
        displayModal(data.message);
        const collectionDiv = document.querySelector('.collection');
        console.log('collectionDiv', collectionDiv)
        collectionDiv.innerHTML = data.html;
        console.log('trickId removed:', trickId, 'action:', action);


        // Réassigner les boutons update-collection
        const addBtns = document.querySelectorAll('.update-collection');
        for (let i = 0; i < addBtns.length; i++) {
          const addBtn = addBtns[i];
          console.log('AddBtn resigned:', addBtn);

          addBtn.addEventListener('click', () => {
            let trickId = addBtn.dataset.trick;
            console.log('trickId', trickId)
            const action = addBtn.dataset.action;
            updateCollection(trickId, action, displayModal);
          });
        }
      }
    });
}


