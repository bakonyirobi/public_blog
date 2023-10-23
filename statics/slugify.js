const titleInput = document.querySelector('input[name=title]');
const slugInput = document.querySelector('input[name=slug]');

const slugify = (val) => {

    return val.toString().toLowerCase().trim()
        .replace(/é/g, 'e')
        .replace(/[óöő]/g, 'o')
        .replace(/[úüű]/g, 'u')
        .replace(/á/g, 'a')
        .replace(/í/g, 'i')
        .replace(/&/g, '-and-')         // Replace & with 'and'
        .replace(/[\s\W-]+/g, '-')      // Replace spaces, non-word characters and dashes with a single dash (-)

};

titleInput.addEventListener('keyup', (e) => {
    slugInput.setAttribute('value', slugify(titleInput.value));
});
