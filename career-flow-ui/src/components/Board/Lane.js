import React,{useContext} from 'react';
import {BoardContext} from './Board'
import CardItem from './CardItem'
function Lane(props) {
    const {taskState,onDragStartHandler,onDragOverHandler} = useContext(BoardContext);
    return (
        <>
      {
        taskState
          .filter(x => x.stage === props.stage.id)
          .map((item, index) => (
            <div className="card-item-container" draggable
              key={index}
              onDragStart={(event) =>
                onDragStartHandler(event, item.id, props.stage.id)
              }
              onDragOver={(event) =>
                onDragOverHandler(event)
              }
            >
              <CardItem  state={props.state}  task={item}/>
            </div>
          ))
      }
    </>
    )
}

export default Lane
