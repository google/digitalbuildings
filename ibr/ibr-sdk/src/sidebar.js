/**
 * @fileoverview This file contains functions that parses the IBRObject
  and creates the sidebar in the UI.
 * @author shuanglihtk@google.com (Shuang Li)
 */

'use strict';

import {IBRObject} from './IBRObject.js';
import {renderSingleIBRStructure, render} from './renderers.js';

/**
 * Create a side bar for visualization and structure navigation.
 * @param {IBRObject} ibrObject IBRObject created from IBR binary data file.
 * @param {HTMLElement} parentElement Parent element to attach the sidebar to.
 * @param {Object} scene The Scene Object that all THREE objects are
  rendered on.
 */
function createSidebar(ibrObject, parentElement, scene) {
  const li = document.createElement('li'); // list element container
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
  const structure = renderSingleIBRStructure(ibrObject, 0, scene);
  drawSingleStructureSidebar(structure, ibrObject.getName(), scene);
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
 */
function createCheckboxForVisualization(visualization, visualizationName,
    structureName) {
  const checkBox = document.createElement('INPUT');
  const div = document.createElement('DIV');
  checkBox.setAttribute('type', 'checkbox');
  checkBox.setAttribute('id', structureName + '_' + visualizationName);
  div.appendChild(checkBox);
  createLabel('label', visualizationName, div, structureName + '_' +
  visualizationName);
  document.getElementById(structureName).appendChild(div);
  checkBox.addEventListener('change', function() {
    if (checkBox.checked) {
      for (const line of visualization) {
        line.visible = true;
      }
    } else {
      for (const line of visualization) {
        line.visible = false;
      }
    }
  });
}

/**
 * Create checkboxes for given structure's visualizations and child structures.
 * @param {Object} structure the structure generated from
 renderSingleIBRStructure() that will be added to sidebar.
 * @param {String} structureName the name of the structure being processed.
 * @param {Object} scene The Scene Object that all THREE objects are
  rendered on.
 */
function drawSingleStructureSidebar(structure, structureName, scene) {
  // Create checkbox for Blocking Grid
  if (structure['blockingGrid']) {
    createCheckboxForVisualization(
        structure['visualizations'][structure['blockingGrid']],
        structure['blockingGrid'], structureName);
  }
  // Create checkbox for each visualization
  if (structure['visualizations'].size !== 0) {
    for (const [visualizationName, visualization] of
      Object.entries(structure['visualizations'])) {
      createCheckboxForVisualization(visualization, visualizationName,
          structureName);
    }
  }

  // Create label for each child structure
  for (let structureIndex = 0; structureIndex <
  structure['structures'].length; structureIndex++) {
    const li = document.createElement('li');
    document.getElementById(structureName).appendChild(li);
    const label = createLabel('span',
        structure['structures'][structureIndex].name, li);
    label.setAttribute('class', 'arrow');
    li.appendChild(label);
    const ul = document.createElement('ul');
    ul.setAttribute('class', 'nested');
    ul.setAttribute('id', structure['structures'][structureIndex].name);
    li.appendChild(ul);
    label.addEventListener('click', function() {
      label.parentElement.querySelector('.nested').classList.toggle('active');
      label.classList.toggle('expanded-arrow');
      if (label.getAttribute('value') == null) {
        event.stopPropagation();
        const curStructure = renderSingleIBRStructure(
            new IBRObject(structure['structures'][structureIndex]),
            structureIndex, scene);
        drawSingleStructureSidebar(curStructure,
            structure['structures'][structureIndex].name, scene);
        label.setAttribute('value', '0');
      }
    });
  }
}

/**
 * Render top level structure in IBRObject and create a side bar for
 visualization and structure navigation.
 * @param {IBRObject} ibrObject IBRObject created from IBR binary data file.
 * @param {number} structureIndex Index of current structure(floor).
 * @param {HTMLElement} renderParentElement Parent element to attach the
 rendering to.
 * @param {HTMLElement} sidebarParentElement Parent element to attach the
 sidebar to.
 */
function renderAndCreateSidebar(ibrObject, structureIndex,
    renderParentElement, sidebarParentElement) {
  const scene = render(ibrObject, structureIndex, renderParentElement);
  createSidebar(ibrObject, sidebarParentElement, scene);
}

export {createSidebar, renderAndCreateSidebar};
