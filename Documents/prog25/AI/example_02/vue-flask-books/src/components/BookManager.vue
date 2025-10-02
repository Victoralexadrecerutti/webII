<template>
  <div>
    <h2>Add New Book</h2>
    <form @submit.prevent="createBook">
      <input v-model="newBook.title" placeholder="Title" required />
      <input v-model="newBook.authors" placeholder="Authors" required />
      <input v-model.number="newBook.year" placeholder="Year" required />
      <input v-model="newBook.publisher" placeholder="Publisher" required />
      <button type="submit">Add Book</button>
    </form>

    <hr />

    <h2>Books</h2>
    <ul>
      <li v-for="book in books" :key="book.id">
        <strong>{{ book.title }}</strong> by {{ book.authors }} ({{ book.year }}) - {{ book.publisher }}
        <button @click="editBook(book)">Edit</button>
        <button @click="deleteBook(book.id)">Delete</button>
      </li>
    </ul>

    <div v-if="editing">
      <h3>Edit Book</h3>
      <form @submit.prevent="updateBook">
        <input v-model="editing.title" />
        <input v-model="editing.authors" />
        <input v-model.number="editing.year" />
        <input v-model="editing.publisher" />
        <button type="submit">Save</button>
        <button @click="cancelEdit">Cancel</button>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

const books = ref([])

// variável que está ligada aos campos (entradas/inputs) da tela'
const newBook = ref({
  title: '',
  authors: '',
  year: null,
  publisher: ''
})

const editing = ref(null)

// const API = 'http://191.52.6.20:5000/books'
const API = 'https://hylsonvescovi.pythonanywhere.com/books'

const fetchBooks = async () => {
  const res = await axios.get(API)
  books.value = res.data
}

const createBook = async () => {
  await axios.post(API, newBook.value)
  newBook.value = { title: '', authors: '', year: null, publisher: '' }
  fetchBooks()
}

const deleteBook = async (id) => {
  await axios.delete(`${API}/${id}`)
  fetchBooks()
}

const editBook = (book) => {
  editing.value = { ...book }
}

const cancelEdit = () => {
  editing.value = null
}

const updateBook = async () => {
  const id = editing.value.id
  const { title, authors, year, publisher } = editing.value
  await axios.put(`${API}/${id}`, { title, authors, year, publisher })
  editing.value = null
  fetchBooks()
}

onMounted(fetchBooks)
</script>

<style scoped>
form input {
  margin: 4px;
  padding: 6px;
}
button {
  margin: 4px;
}
</style>
