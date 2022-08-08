function App() {
    // 새로고침 떄 마다 시행
    this.init = () => {
      console.log(getCookie("modal-closed"));
      if (getCookie("modal-closed") === "true") {
        closeModal();
        return;
      }
      openModal();
    };
  
    // 모달 생성
    const body = document.querySelector("body");
    const modal = document.querySelector(".modal-container");
    const close = document.querySelector(".modal-close");
    const neverSee = document.querySelector(".modal-stop-button");
    const openmodelbtn = document.querySelector(".modal-open-button");

    neverSee.addEventListener("click", () => {
      closeModal();
      setCookie("modal-closed", "true", 1);
    });
  
    modal.addEventListener("click", (event) => {
      if (event.target === modal) {
        closeModal();
      }
    });
  
    openmodelbtn.addEventListener("click", openModal);
    close.addEventListener("click", closeModal);
  
    function openModal() {
      modal.classList.add("open");
      body.style.overflow = "hidden";
    };
  
    function closeModal() {
      modal.classList.remove("open");
      body.style.overflow = "auto";
    };
  

    //쿠키
    const setCookie = (name, value, expireDate) => {
      let today = new Date();
      today.setDate(today.getDate() + expireDate);
      document.cookie = `${name}=${value};expires=${today.toGMTString()}`;
    };
  
    const getCookie = (name) => {
      let cookie = document.cookie;
      if (document.cookie) {
        let cookies = cookie.split("; ");
        for (let index in cookies) {
          let cookieName = cookies[index].split("=");
          if (cookieName[0] === name) {
            return cookieName[1];
          }
        }
      }
      return;
    };
}

const app = new App();
app.init();