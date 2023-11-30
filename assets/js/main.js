const hamburgerBtn = document.querySelector('#menu-toggle')
hamburgerBtn.addEventListener('click', () => {
    const sidebar = document.querySelector('#sidebar-wrapper')
    sidebar.classList.toggle('toggled')
})

// AKUN
function changeProfilePic() {
    const input = document.getElementById('profilePicUpload');
    const img = document.getElementById('profilePic');
    const file = input.files[0];
  
    if (file) {
      const reader = new FileReader();
      reader.onload = function (e) {
        img.src = e.target.result;
      };
      reader.readAsDataURL(file);
    }
  }
  
  // Tambahkan event listener untuk memanggil changeProfilePic saat input file berubah
  document.getElementById('profilePicUpload').addEventListener('change', changeProfilePic);
  
  