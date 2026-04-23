function bear() {
  const url = `https://placebear.com/${200 + Math.floor(Math.random()*100)}/${300 + Math.floor(Math.random()*100)}`;

  document.getElementById("image").innerHTML =`<img src="${url}" alt="Bear" width="320" />`;
}