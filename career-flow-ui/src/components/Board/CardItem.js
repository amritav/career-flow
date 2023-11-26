import React, { useState, useContext } from "react";
import { BoardContext } from "./Board";
import TaskForm from "./New Task/TaskForm";
import { Card, CardContent, Typography, IconButton, CardActions, Divider, Box, Stack } from "@mui/material";
import EditIcon from '@mui/icons-material/Edit';
import DeleteIcon from '@mui/icons-material/Delete';
import { makeStyles } from '@mui/styles';
import axios from 'axios';
import { Dialog, DialogTitle, DialogContent, DialogActions, TextField, Button } from '@mui/material';
import ShareIcon from '@mui/icons-material/Share';
import DescriptionIcon from '@mui/icons-material/Description';


const useStyles = makeStyles({
  cardHover: {
    position: 'relative',
    '&:hover $cardActions': {
      display: 'block'
    }
  },
  cardActions: {
    display: 'none',
    position: 'absolute',
    top: 0,
    right: 0,
    backgroundColor: 'rgba(255, 255, 255, 0.9)' // Optional: add background for visibility
  },
  smallIcon: {
    fontSize: '16px'
  }
});

// Function to format the date
const formateDate = (date) => {
  const months = [
    "Jan", "Feb", "Mar", "Apr", "May", "Jun",
    "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
  ];

  const month = months[date.getMonth()];
  let day = "" + date.getDate();

  if (day.length < 2) day = "0" + day;

  return `${month} ${day}, ${date.getFullYear()}`;
};

const initialEditedValues = {
  id: "",
  jobTitle: "",
  companyName: "",
  date: new Date(),
  jobLink: "",
  location: ""
};

function CardItem(props) {
  const classes = useStyles();
  const [show, setShow] = useState(false);
  const [editedValues, setFormValues] = useState(initialEditedValues);
  const { taskState, onDeletingTask, onUpdatingTask } = useContext(BoardContext);

  const [email, setEmail] = useState('');
  const [openModal, setOpenModal] = useState(false);

  const handleOpenModal = () => setOpenModal(true);
  const handleCloseModal = () => setOpenModal(false);

  const [showNotesModal, setShowNotesModal] = useState(false);
  const [notes, setNotes] = useState(props.task.notes || []);

  const handleOpenNotesModal = () => setShowNotesModal(true);
  const handleCloseNotesModal = () => setShowNotesModal(false);


  const handleShare = () => {
    // API call to backend with email and task details
    axios.post('/sendEmail', {
      email: email,
      taskDetails: props.task
    }, {
      headers: {
        'Authorization': "Bearer " + localStorage.getItem("token") // Attach the Authorization header
      }
    }).then(response => {
      // Handle success
      console.log('Email sent successfully');
      handleCloseModal();
    }).catch(error => {
      // Handle error
      console.error('Error sending email', error);
    });
  };

  const handleClose = () => setShow(false);

  const deleteTask = (taskId) => {
    axios.delete('/applications/' + taskId, {
      headers: {
        Authorization: "Bearer " + localStorage.getItem("token"),
      }
    })
      .then(response => {
        console.log('Task deleted:', response);
        onDeletingTask(taskId); // existing function to update the state
      })
      .catch(error => {
        console.error('Error deleting task:', error);
      });
  };

  const updateTask = (updatedTask) => {
    axios.put(`/applications/${updatedTask.id}`, { application: updatedTask }, {
      headers: {
        Authorization: "Bearer " + props.state.token,
      }
    })
      .then(response => {
        onUpdatingTask(response.data); // Update the state in the context
      })
      .catch(error => console.error('Error updating task:', error));
  };


  const handleShow = () => {
    setShow(true);
  };

  const clickHandler = (type) => {
    if (type === "edit") {
      const formValues = taskState.find((task) => task.id === props.task.id);
      setFormValues(formValues);
      handleShow();
    } else if (type === "delete") {
      deleteTask(props.task.id);
    }
  };

  const handleUpdate = (values, submitProps) => {
    submitProps.setSubmitting(false);
    updateTask(values); // Call the updateTask function with the new values
    setShow(false);
    submitProps.resetForm();


  };

  const handleNoteChange = (event, index) => {
    const updatedNotes = [...notes];
    updatedNotes[index] = event.target.value;
    setNotes(updatedNotes);
  };

  const handleAddNote = () => {
    const updatedNotes = [...notes, ""];
    setNotes(updatedNotes);
  };

  const handleSaveNotes = () => {

    axios.put(`/applications/${props.task.id}`, { notes: notes }, {
      headers: {
        Authorization: "Bearer " + props.state.token,
      }
    })
      .then(response => {
        // Handle success
      })
      .catch(error => {
        // Handle error
      });

    handleCloseNotesModal();
  };

  return (
    <>
      <TaskForm
        editedValues={editedValues}
        taskState="Update"
        show={show}
        handleClose={handleClose}
        onSubmit={handleUpdate}
      />
      <Card key={props.task.id} variant="outlined" className={classes.cardHover}>
        <CardContent>
          <Typography variant="h5" component="div">
            {props.task.companyName}
          </Typography>
          <Typography variant="body2">
            {props.task.jobTitle}
          </Typography>
          <Typography variant="body2" color="textSecondary">
            Date: {formateDate(new Date(props.task.date))}
          </Typography>
        </CardContent>
        <Box style={{ position: 'relative' }}>
          <IconButton onClick={handleOpenNotesModal} style={{ position: 'absolute', bottom: 10, right: 8, }}>
            <DescriptionIcon className={classes.smallIcon} />
          </IconButton>
        </Box>

        <CardActions className={classes.cardActions}>
          <IconButton onClick={() => clickHandler("edit")} aria-label="edit">
            <EditIcon className={classes.smallIcon} />
          </IconButton>
          <IconButton onClick={() => clickHandler("delete")} aria-label="delete">
            <DeleteIcon className={classes.smallIcon} />
          </IconButton>
          <IconButton onClick={handleOpenModal} aria-label="share">
            <ShareIcon className={classes.smallIcon} />
          </IconButton>
        </CardActions>
      </Card>

      <Dialog open={openModal} onClose={handleCloseModal} >
        <DialogTitle align='center' fontWeight='bold'>Share Task</DialogTitle>
        <Divider />
        <DialogContent>
          <Box display="flex">
            <Typography sx={{ mt: 1.5 }}>Enter Email Address: </Typography>
            <TextField
              autoFocus
              margin="dense"
              label="Email Address"
              type="email"
              fullWidth
              variant="outlined"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
            />
          </Box>
        </DialogContent>
        <DialogActions>
          <Button variant="outlined" onClick={handleCloseModal}>Cancel</Button>
          <Button variant="contained" onClick={handleShare}>Send</Button>
        </DialogActions>
      </Dialog>

      <Dialog open={showNotesModal} onClose={handleCloseNotesModal} fullWidth maxWidth="xs">
        <DialogTitle align='center' fontWeight='bold'>Notes</DialogTitle>
        <Divider />
        <DialogContent>
          {notes.map((note, index) => (
            <Box key={index} marginBottom={2}>
              {note ? (
                <Box padding={1} borderRadius={4}>
                  <Typography>{note}</Typography>
                </Box>
              ) : (
                // <Box
                //   border="2px dashed #bdbdbd"
                //   borderRadius={4}
                //   minHeight={50}
                //   display="flex"
                //   alignItems="center"
                //   justifyContent="center"
                //   onClick={(e) => handleNoteChange(e, index)}
                // >
                <TextField fullWidth multiline={true} rows={3} placeholder="Add Note" 
                // variant="standard"
                // InputProps={{
                //   disableUnderline: true,
                // }}
                >

                </TextField>
                // </Box>
              )}
            </Box>
          ))}
          <IconButton onClick={handleAddNote} aria-label="add-note">
            <DescriptionIcon className={classes.smallIcon} />
          </IconButton>
        </DialogContent>
        <DialogActions>
          <Button variant="outlined" onClick={handleCloseNotesModal}>Cancel</Button>
          <Button variant="contained" onClick={handleSaveNotes}>Save</Button>
        </DialogActions>
      </Dialog>

    </>
  );
}

export default CardItem;
