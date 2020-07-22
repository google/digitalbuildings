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
      const out = IBRSDK.render( bin,
          0, document.getElementById('mainCanvas') ); // top level, index 0
      IBRSDK.createSidebar( bin, document.getElementById('layerList') );
      document.getElementById('dwn-btn')
          .addEventListener('click', function(){
            download( "out.ibr", out );
          });
    };
    fr.readAsArrayBuffer(file);
  }
}

/**
 * Create binary file from data and download the file in browser.
 * @param {String} filename name of the binary file that will be created.
 * @param {Buffer} bin binary data that will be saved in the file.
 */
function download( filename, bin ) {

  const element = document.createElement('a');
  const blob = new Blob([bin], {type: 'application/octet-stream'});
  const url = window.URL.createObjectURL(blob);
  element.setAttribute('href', url);
  element.setAttribute('download', filename);

  element.style.display = 'none';
  document.body.appendChild(element);

  element.click();

  document.body.removeChild(element);

}

document.getElementById('fileForUpload')
    .addEventListener('change', onChooseFile);
