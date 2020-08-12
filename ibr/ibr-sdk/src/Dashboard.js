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
    background: '#2d2d2d',
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

/**
 * Create the Dashboard UI components.
 * @return {Object} Dashboard UI components in React Tags.
 */
function Dashboard() {
  const classes = useStyles();

  return (
    <div className={classes.root}>
      <CssBaseline />
      <AppBar position="absolute" className={clsx(classes.appBar)}>
        <Toolbar className={classes.toolbar}>
          <Typography component="h1" variant="h6" color="inherit" noWrap
            className={classes.title} style={{flex: 1}}>
            IBR Demo
          </Typography>
          <label htmlFor="fileForUpload">
            <input type="file" id="fileForUpload" onChange={onChooseFile}
              style={{display: 'none'}}/>
            <Button
              variant="contained"
              style={{background: '#1a73e8', color: 'white'}}
              component="span">
              Upload IBR
            </Button>
          </label>
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
