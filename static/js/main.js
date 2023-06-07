let root =  document.documentElement
//document.addEventListener('mousemove', e => {
//  root.style.setProperty('--mouse-x', e.x);
//  root.style.setProperty('--mouse-y', e.y);
//});
root.style.setProperty('--client-width', document.documentElement.clientWidth)
root.style.setProperty('--client-height', document.documentElement.clientHeight)

window.onresize = function(event) {
    root.style.setProperty('--client-width', document.documentElement.clientWidth)
    root.style.setProperty('--client-height', document.documentElement.clientHeight)
};