<template>
  <div class="transcript__container">
    <form @submit.prevent="submitForm" class="transcript__form">
      <div class="transcript__form-link-input">
        <label for="youtubeLink">YouTube Link:</label>
        <input id="youtubeLink" v-model="youtubeLink" placeholder="Enter YouTube link" :disabled="isLoading" />
      </div>
      <div class="transcript__form-audio-input">
        <label for="audioFile">Audio File: {{ }}</label>
        <input :key="audioFileKey" id="audioFile" type="file" accept="audio/*" @change="handleAudioFileChange"
          :disabled="isLoading" />
      </div>
      <button class="transcript__form-submit-button type=" submit :disabled="isLoading">Submit</button>
    </form>
    <section class="transcript__summary" v-if="shouldShowInfoSection">
      <h2>Summary | Type: {{ type }}</h2>
      <p>{{ summary }}</p>
      <h2>Transcription</h2>
      <p>{{ transcription }}</p>
    </section>
    <section class="transcript__loading-indicator" v-else-if="isLoading">
      <p>Waiting for transcription...</p>
    </section>
  </div>
</template>

<style scoped>
.transcript__container {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin: 100px auto;
  gap: 32px;
}
</style>

<script setup>
import { ref, computed } from 'vue'
import axios from 'axios'

const youtubeLink = ref('')
const audioFile = ref(null)
const audioFileKey = ref(0)
const summary = ref('')
const transcription = ref('')
const type = ref('')
const isLoading = ref(false)

const shouldShowInfoSection = computed(() => {
  return summary.value && transcription.value && type.value
})

const submitForm = () => {
  isLoading.value = true
  resetDataField()
  if (!youtubeLink.value && !audioFile.value) {
    alert('Please fill in either the YouTube link or upload an audio file.')
    isLoading.value = false
    return
  }

  let formData = new FormData()
  youtubeLink.value
    ? formData.append('link', youtubeLink.value)
    : formData.append('audio', audioFile.value)

  axios
    .post('http://localhost:5000/transcribe', formData)
    .then(response => {
      const data = response.data
      summary.value = data.summary
      transcription.value = data.transcription
      type.value = data.type
      isLoading.value = false
      resetForm()
    })
    .catch((error) => {
      console.error('error', error)
      isLoading.value = false
    })
}

const resetDataField = () => {
  summary.value = ''
  transcription.value = ''
  type.value = ''
}

const resetForm = () => {
  audioFile.value = ''
  audioFileKey.value++ //key force re render method
  youtubeLink.value = ''
}

const handleAudioFileChange = (event) => {
  audioFile.value = event.target.files[0]
}
</script>
