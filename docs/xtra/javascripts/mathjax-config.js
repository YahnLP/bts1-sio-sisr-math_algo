/* Formules en MathJax 3 : \( … \) en ligne, \[ … \] en bloc (balises produites par pymdownx.arithmatex) */
window.MathJax = {
  tex: { inlineMath: [["\\(", "\\)"]], displayMath: [["\\[", "\\]"]], processEscapes: true, processEnvironments: true },
  options: { ignoreHtmlClass: ".*|", processHtmlClass: "arithmatex" }
};
document$.subscribe(() => {
  if (window.MathJax && MathJax.typesetPromise) { MathJax.startup.output.clearCache(); MathJax.typesetClear(); MathJax.texReset(); MathJax.typesetPromise(); }
});
