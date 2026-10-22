import mongoose from 'mongoose';

const LessonSchema = new mongoose.Schema({
  title: { type: String, required: true },
  youtubeUrl: { type: String, required: true },
  videoId: { type: String, required: true },
  durationMin: { type: Number, default: 0 },
  lessonOrder: { type: Number, default: 0 },
  quizData: { type: Array, default: [] }
});

const CourseSchema = new mongoose.Schema({
  title: { type: String, required: true },
  description: { type: String, default: '' },
  skillTopic: { type: String, required: true },
  nmTrack: { type: String, required: true },
  thumbnail: { type: String, default: '' },
  lessons: [LessonSchema],
  createdAt: { type: Date, default: Date.now }
});

export default mongoose.model('Course', CourseSchema);
