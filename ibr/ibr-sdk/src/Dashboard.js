import React from 'react';
import ReactDOM from 'react-dom';
import clsx from 'clsx';
import {makeStyles} from '@material-ui/core/styles';
import CssBaseline from '@material-ui/core/CssBaseline';
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import Typography from '@material-ui/core/Typography';
import Button from '@material-ui/core/Button';

const useStyles = makeStyles((theme) => ({
  root: {
    display: 'flex',
  },
  toolbar: {
    paddingRight: 24, // keep right padding when drawer closed
    flexDirection: 'row',
    justifyContent: 'spaceBetween',
  },
  main: {
    marginLeft: 300,
  },
  appBar: {
    zIndex: theme.zIndex.drawer + 1,
    transition: theme.transitions.create(['width', 'margin'], {
      easing: theme.transitions.easing.sharp,
      duration: theme.transitions.duration.leavingScreen,
    }),
  },
  title: {
    flexGrow: 1,
  },
  appBarSpacer: theme.mixins.toolbar,
  content: {
    flexGrow: 1,
    height: '100vh',
    overflow: 'auto',
    paddingLeft: 300,
  },
  paper: {
    padding: theme.spacing(2),
    display: 'flex',
    overflow: 'auto',
    flexDirection: 'column',
  },
  fixedHeight: {
    height: 240,
  },
}));

/**
 * Create binary file from data and download the file in browser.
 * @param {String} filename name of the binary file that will be created.
 * @param {Buffer} binary data that will be saved in the file.
 */
function download(filename, ibrObject, floorsToSave) {
  const bin = IBRSDK.saveToBuffer(ibrObject, floorsToSave);
  const element = document.createElement('a');
  const blob = new Blob([bin], {type: 'application/octet-stream'});
  const url = window.URL.createObjectURL(blob);
  element.setAttribute('href', url);
  element.setAttribute('download', filename+'.ibr');
  element.style.display = 'none';
  document.body.appendChild(element);
  element.click();
  document.body.removeChild(element);
}


/**
 * Create the Dashboard UI components.
 * @return {Object} Dashboard UI components in React Tags.
 */
function Dashboard() {
  const classes = useStyles();

  /**
   * Parse the input IBR file using IBRSDK.
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
        const ibrObject = IBRSDK.init(bin);

        console.log(Dashboard);
        Dashboard.ibrObject = ibrObject;
        console.log(Dashboard.ibrObject);

        const floorsToSave = [];
        IBRSDK.renderAndCreateSidebar(ibrObject,
            document.getElementById('mainCanvas'),
            document.getElementById('layerList'), floorsToSave);
        document.getElementById('dwn-btn')
            .addEventListener('click', function() {
              // TODO(realkevinwang): why is download defined in index.html?
              download(document.getElementById('filename').value, ibrObject,
                  floorsToSave);
            });
      };
      fr.readAsArrayBuffer(file);
    }
  }

  function rerenderSidebar() {
    IBRSDK.renderAndCreateSidebar(
      Dashboard.ibrObject,
      document.getElementById('mainCanvas'),
      document.getElementById('layerList'),
      []);
  }

  return (
    <div className={classes.root}>
      <CssBaseline />
      <AppBar position="absolute" className={clsx(classes.appBar)}>
        <Toolbar className={classes.toolbar}>
          <Typography component="h1" variant="h6" color="inherit" noWrap
            className={classes.title} style={{flex: 1}}>
            IBR Demo
          </Typography>
          <label htmlFor="fileForUpload" style={{flex: 1}}>
            <input type="file" id="fileForUpload" onChange={onChooseFile}
              style={{display: 'none'}}/>
            <Button
              variant="contained"
              style={{background: '#1a73e8', color: 'white'}}
              component="span">
              Upload IBR
            </Button>
          </label>
          <div className="mode-toggle">
            <p>Visual</p>
            <label className="switch">
              <input type="checkbox" id="mode" onChange={rerenderSidebar}/>
              <span className="slider round"></span>
            </label>
            <p>Export</p>
          </div>
        </Toolbar>
      </AppBar>
      <main className={classes.content}>
        <div className={classes.appBarSpacer} />
        <div id="mainCanvas"/>
      </main>
    </div>
  );
}

/**
 * Render the Dashboard component.
 */
function createDashboard() {
  ReactDOM.render(<Dashboard />, document.querySelector('#dashboard'));
}

export {createDashboard};
