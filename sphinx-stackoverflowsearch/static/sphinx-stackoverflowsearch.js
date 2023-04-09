function createSection() {
  if (document.querySelector('#stackoverflow')) {
    return;
  }
  const section = document.createElement('section');
  section.id = 'stackoverflow';
  const title = document.createElement('h2');
  title.id = 'stackoverflow-title';
  title.textContent = 'Stack Overflow search results';
  const content = document.createElement('div');
  content.id = 'stackoverflow-results';
  content.textContent = 'Calculating...';
  section.appendChild(title);
  section.appendChild(content);
  const siblingNode = document.querySelector('#search-results');
  const parentNode = siblingNode.parentNode;
  parentNode.insertBefore(section, siblingNode);
}

function getQuery() {
  const params = new URLSearchParams(window.location.search);
  return params.get('q');
}

window.addEventListener('load', () => {
  createSection();
});
