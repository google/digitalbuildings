/**
 * @fileoverview This file contains functions that parses the IBRObject
  and creates the sidebar in the UI.
 * @author shuanglihtk@google.com (Shuang Li)
 */

'use strict';

import {IBRObject} from './IBRObject.js';
import {renderSingleIBRStructure, render} from './renderers.js';
import {BLOCKING_GRID_NAME, BOUNDARY_NAME} from './constants.js';

/**
 * Create a side bar for visualization and structure navigation.
 * @param {IBRObject} ibrObject IBRObject created from IBR binary data file.
 * @param {HTMLElement} parentElement Parent element to attach the sidebar to.
 * @param {Object} scene The Scene Object that all THREE objects are
  rendered on.
 * @param {Map.<String, List<Mesh>>} spaceLib Space library stores space
 name and mesh object(s).
 * @param {Map.<String, List.<String, Line>>} connectionLib Boundary name and
 corresponding list of neighbor names and three.js Line object.
 * @param {List.<Boolean>} floorsToSave Boolean array representing the floors
 to be exported. If element at index i is true, the i-th floor will be
 exported.
 */
function createSidebar(ibrObject, parentElement, scene, spaceLib,
    connectionLib, floorsToSave) {
  const li = document.createElement('li');
  parentElement.appendChild(li);
  const rootSpan = createLabel('span', ibrObject.getName(), li);
  rootSpan.setAttribute('class', 'arrow');
  li.appendChild(rootSpan);
  const ul = document.createElement('ul');
  ul.setAttribute('class', 'nested');
  ul.setAttribute('id', ibrObject.getName());
  li.appendChild(ul);
  rootSpan.addEventListener('click', function() {
    rootSpan.parentElement.querySelector('.nested').classList
        .toggle('active');
    rootSpan.classList.toggle('expanded-arrow');
  });
  // root structure index 0
  const structure = renderSingleIBRStructure(ibrObject, 0, scene, spaceLib,
      connectionLib);
  drawSingleStructureSidebar(structure, ibrObject.getName(), 0, scene,
      spaceLib, connectionLib, floorsToSave);
}

/**
 * Create a new HTML Label Tag based on given name string and attach it to
 * given parent tag.
 * @param {string} tagName Type of tag to be created.
 * @param {string} name InnerHTML of the Label tag.
 * @param {tag} parentTag Tag to be attached to by the newly created label
  tag.
 * @param {string} [forId=undefined] ID to be set as the value of the newly
  created label tag's for attribute. Needed if Label tag is created for a
  checkbox.
 * @return {tag} Newly created Label tag.
 */
function createLabel(tagName, name, parentTag, forId = undefined) {
  const label = document.createElement(tagName);
  if (forId) {
    label.setAttribute('for', forId);
  }
  label.innerHTML = name;
  parentTag.appendChild(label);
  return label;
}

/**
 * Create checkboxes for given visualization.
 * @param {Object} visualization the visualization object to be
 added to the sidebar.
 * @param {String} visualizationName the name of the visualization being
 processed.
 * @param {String} structureName the name of parent structure of the
 visualization.
 * @param {Boolean} isBoundary If the visualization currently being rendered is
 from the boundary field of the ibrObject.
 * @param {List.<Object>} connections List of connections of the current
 structure.
 * @param {Map.<String, List<Mesh>>} spaceLib Space library stores space
 name and mesh object(s).
 * @param {Map.<String, List.<String, Line>>} connectionLib Boundary name and
 corresponding list of neighbor names and three.js Line object.
 */
function createCheckboxForVisualization(visualization, visualizationName,
    structureName, isBoundary=false, connections=null, spaceLib=null,
    connectionLib=null) {
  const checkBox = document.createElement('INPUT');
  const div = document.createElement('DIV');
  checkBox.setAttribute('type', 'checkbox');
  checkBox.setAttribute('class', 'visualMode');
  checkBox.setAttribute('id', structureName + '_' + visualizationName);

  // only show if in visual mode
  if (!document.getElementById('mode').checked) {
    div.appendChild(checkBox);
  }

  createLabel('label', visualizationName, div, structureName + '_' +
  visualizationName);
  document.getElementById(structureName).appendChild(div);

  const neighbors = [];
  if (isBoundary && connectionLib) {
    for (const connection of connectionLib.get(structureName)) {
      neighbors.push([spaceLib.get(connection[0]), connection[1]]);
    }
  }

  checkBox.addEventListener('change', function() {
    if (checkBox.checked) {
      for (const line of visualization) {
        line.visible = true;
      }
      // If space, check connection visibility
      if (isBoundary) {
        for (const connection of connectionLib.get(structureName)) {
          if (spaceLib.get(connection[0])[0].visible) {
            connection[1].visible = true;
          }
        }
      }
    } else {
      for (const line of visualization) {
        line.visible = false;
      }
      // If space, check connection visibility
      if (isBoundary) {
        for (const connection of connectionLib.get(structureName)) {
          connection[1].visible = false;
        }
      }
    }
  });
}

/**
 * Create checkboxes for given structure's visualizations and child structures.
 * @param {Object} structure the structure generated from
 renderSingleIBRStructure() that will be added to sidebar.
 * @param {String} structureName the name of the structure being processed.
 * @param {Number} level The level of the parent structure.
 * @param {Object} scene The Scene Object that all THREE objects are
  rendered on.
 * @param {Map.<String, List<Mesh>>} spaceLib Space library stores space
 name and mesh object(s).
 * @param {Map.<String, List.<String, Line>>} connectionLib Boundary name and
 corresponding list of neighbor names and three.js Line object.
 * @param {List.<Boolean>} floorsToSave Boolean array representing the floors
 to be exported. If element at index i is true, the i-th floor will be
 exported.
 */
function drawSingleStructureSidebar(structure, structureName, level, scene,
    spaceLib, connectionLib, floorsToSave) {
  // Create checkbox for Blocking Grid
  if (structure['blockingGrid']) {
    createCheckboxForVisualization(
        structure['blockingGrid'][BLOCKING_GRID_NAME], BLOCKING_GRID_NAME,
        structureName);
  }

  if (structure['boundary']) {
    createCheckboxForVisualization(
        structure['boundary'][BOUNDARY_NAME], BOUNDARY_NAME,
        structureName, true, structure['boundary']['connections'], spaceLib,
        connectionLib);
  }

  // Create Visualization tag, then in the next section add the Visualizations
  // under space tag.
  const visLi = document.createElement('li');
  document.getElementById(structureName).appendChild(visLi);
  const visSpan = createLabel('span', 'Layers', visLi);
  visSpan.setAttribute('class', 'arrow');

  const visUl = document.createElement('ul');
  visUl.setAttribute('class', 'nested');
  const visUlName = structureName + '_visualizations';
  visUl.setAttribute('id', visUlName);
  visLi.appendChild(visUl);

  visLi.style.display = 'none';
  visSpan.addEventListener('click', function() {
    visSpan.parentElement.querySelector('.nested').classList.toggle('active');
    visSpan.classList.toggle('expanded-arrow');
  });

  // Create checkbox for each visualization
  if (structure['visualizations'].size) {
    visLi.style.display = 'block';
    for (const [visualizationName, visualization] of
      structure['visualizations']) {
      createCheckboxForVisualization(visualization, visualizationName,
          visUlName);
    }
  }

  // Create Space tag, then in the next section add the SPACE sub structures
  // under space tag.
  const spaceLi = document.createElement('li');
  document.getElementById(structureName).appendChild(spaceLi);
  const spaceSpan = createLabel('span', 'Spaces', spaceLi);
  spaceSpan.setAttribute('class', 'arrow');
  const spaceUl = document.createElement('ul');
  spaceUl.setAttribute('class', 'nested');
  const spaceUlName = structureName+'_spaces';
  spaceUl.setAttribute('id', spaceUlName);
  spaceLi.appendChild(spaceUl);
  spaceLi.style.display = 'none';
  spaceSpan.addEventListener('click', function() {
    spaceSpan.parentElement.querySelector('.nested').classList.toggle('active');
    spaceSpan.classList.toggle('expanded-arrow');
  });

  // Create label for each child structure
  for (let structureIndex = 0; structureIndex <
  structure['structures'].length; structureIndex++) {
    let parentTagName = '';
    const curIBRObject = new IBRObject(structure['structures'][structureIndex]);
    if (curIBRObject.getStructuralType() ===
    InternalBuildingRepresentation.StructuralType['SPACE'].value) {
      parentTagName = spaceUlName;
      spaceLi.style.display = 'block';
    } else {
      parentTagName = structureName;
    }
    const li = document.createElement('li');
    document.getElementById(parentTagName).appendChild(li);

    // creates checkbox for save back to IBR feature
    if (level === 0 && curIBRObject.getStructuralType() !==
        InternalBuildingRepresentation.StructuralType['SPACE'].value) {
      floorsToSave[structureIndex] = false;
      const checkBox = document.createElement('INPUT');
      checkBox.setAttribute('type', 'checkbox');
      checkBox.setAttribute('class', 'exportMode');

      // only show if in export mode
      if (document.getElementById('mode').checked) {
        li.appendChild(checkBox);
      }

      checkBox.addEventListener('change', function() {
        if (checkBox.checked) {
          floorsToSave[structureIndex] = true;
        } else {
          floorsToSave[structureIndex] = false;
        }
      });
    }

    const label = createLabel('span',
        curIBRObject.getName(), li);
    label.setAttribute('class', 'arrow');
    const ul = document.createElement('ul');
    ul.setAttribute('class', 'nested');
    ul.setAttribute('id', curIBRObject.getName());
    li.appendChild(ul);
    let height;
    if (curIBRObject.getStructuralType() ===
    InternalBuildingRepresentation.StructuralType['SPACE'].value) {
      height = level;
    } else {
      height = structureIndex;
    }
    label.addEventListener('click', function() {
      label.parentElement.querySelector('.nested').classList.toggle('active');
      label.classList.toggle('expanded-arrow');
      if (!label.getAttribute('value')) {
        event.stopPropagation();
        const curStructure = renderSingleIBRStructure(
            curIBRObject, height, scene, spaceLib, connectionLib);
        drawSingleStructureSidebar(curStructure,
            curIBRObject.getName(), height, scene, spaceLib, connectionLib,
            floorsToSave);
        label.setAttribute('value', '0');
      }
    });
  }
}

/**
 * Render top level structure in IBRObject and create a side bar for
 visualization and structure navigation.
 * @param {IBRObject} ibrObject IBRObject created from IBR binary data file.
 * @param {HTMLElement} renderParentElement Parent element to attach the
 rendering to.
 * @param {HTMLElement} sidebarParentElement Parent element to attach the
 sidebar to.
 * @param {List.<Boolean>} floorsToSave Boolean array representing the floors
 to be exported. If element at index i is true, the i-th floor will be
 exported.
 */
function renderAndCreateSidebar(ibrObject,
    renderParentElement, sidebarParentElement, floorsToSave) {
  /* Each of the two functions are also published. Understanding of usage of
     scene in THREE is required if user desires to use any one function
     without the other. */
  const spaceLib = new Map();
  const connectionLib = new Map();
  renderParentElement.innerHTML = '';
  sidebarParentElement.innerHTML = '';
  const scene = render(ibrObject, renderParentElement, spaceLib,
      connectionLib);
  createSidebar(ibrObject, sidebarParentElement, scene, spaceLib,
      connectionLib, floorsToSave);
}

export {createSidebar, renderAndCreateSidebar};
