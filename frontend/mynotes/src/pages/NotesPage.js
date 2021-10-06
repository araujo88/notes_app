import React from 'react'
import notes from '../assets/data'
import ListItem from '../components/ListItem'

const NotesPages = () => {
    return (
        <div>
            {notes.map(note => (
                <ListItem note={note}/>
            ))}
        </div>
    )
}

export default NotesPages
