const hamburgerBtn = document.querySelector('#menu-toggle')
hamburgerBtn.addEventListener('click', () => {
    const sidebar = document.querySelector('#sidebar-wrapper')
    sidebar.classList.toggle('toggled')
})