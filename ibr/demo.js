/**
 * @fileoverview This file takes a binary wire format ibr file, decode the
 information and store data in sessionStorage for visualization use.
 * @author shuanglihtk@google.com (Shuang Li)
 */

/**
 * Setup THREE.js environment and extract top level structure once an IBR
 file is given.
 */
function onChooseFile() {
  if (typeof window.FileReader !== 'function') {
    throw new Error('The file API isn\'t supported on this browser.');
  }
  const file = document.getElementById('fileForUpload').files[0];
  if (file) {
    const fr = new FileReader();
    fr.onload = function(evt) {
      const bin = evt.target.result;
      IBRSDK.render( bin,
          0, document.getElementById('mainCanvas') ); //top level, index 0
      IBRSDK.createSidebar( bin, document.getElementById('layerList') );
    };
    fr.readAsArrayBuffer(file);
  }
}

document.getElementById('fileForUpload')
    .addEventListener('change', onChooseFile);
