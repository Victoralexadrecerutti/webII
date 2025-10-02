<template>
  <div class="container">
    <h1>Person CRUD</h1>

    <!-- Add Person Form -->
    <form @submit.prevent="addPerson" class="form">
      <input v-model="newPerson.name" placeholder="Name" required />
      <input v-model="newPerson.email" placeholder="Email" required />
      <input v-model="newPerson.phone" placeholder="Phone" required />
      <input v-model="newPerson.dob" placeholder="DOB (YYYY-MM-DD)" required />
      <button type="submit">Add Person</button>
    </form>

    <!-- Person List -->
    <table>
      <thead>
        <tr>
          <th>ID</th><th>Name</th><th>Email</th><th>Phone</th><th>DOB</th><th>Actions</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="person in people" :key="person.id">
          <td>{{ person.id }}</td>
          <td v-if="editId !== person.id">{{ person.name }}</td>
          <td v-else><input v-model="editPerson.name" /></td>

          <td v-if="editId !== person.id">{{ person.email }}</td>
          <td v-else><input v-model="editPerson.email" /></td>

          <td v-if="editId !== person.id">{{ person.phone }}</td>
          <td v-else><input v-model="editPerson.phone" /></td>

          <td v-if="editId !== person.id">{{ person.dob }}</td>
          <td v-else><input v-model="editPerson.dob" /></td>

          <td>
            <button v-if="editId !== person.id" @click="startEdit(person)">Edit</button>
            <button v-else @click="saveEdit(person.id)">Save</button>
            <button @click="deletePerson(person.id)">Delete</button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';

const API = 'http://localhost:5000/persons';

const people = ref([]);
const newPerson = ref({ name: '', email: '', phone: '', dob: '' });

const editId = ref(null);
const editPerson = ref({});

const fetchPeople = async () => {
  const res = await axios.get(API);
  people.value = res.data;
};

const addPerson = async () => {
  await axios.post(API, newPerson.value);
  newPerson.value = { name: '', email: '', phone: '', dob: '' };
  fetchPeople();
};

const deletePerson = async (id) => {
  await axios.delete(`${API}/${id}`);
  fetchPeople();
};

const startEdit = (person) => {
  editId.value = person.id;
  editPerson.value = { ...person };
};

const saveEdit = async (id) => {
  await axios.put(`${API}/${id}`, editPerson.value);
  editId.value = null;
  fetchPeople();
};

onMounted(fetchPeople);
</script>

<style>
.container {
  max-width: 800px;
  margin: auto;
  padding: 2rem;
}
.form input {
  margin: 0.25rem;
}
table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 2rem;
}
th, td {
  border: 1px solid #ccc;
  padding: 0.5rem;
}
</style>
