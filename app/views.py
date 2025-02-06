from rest_framework import viewsets, serializers
from rest_framework.response import Response
from .models import Question, StudentProgress
from .utils import generate_similar_questions

# Create your views here.
class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'

class StudentProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentProgress
        fields = '__all__'

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def create(self, request, *args, **kwargs):
        question_text = request.data.get("text")
        is_correct = request.data.get("is_correct")
        student_id = request.data.get("student_id")

        # Record attempt
        StudentProgress.objects.create(
            student_id=student_id,
            question=Question.objects.get(text=question_text),
            is_correct=is_correct
        )

        if not is_correct:
            # generate a similar question
            new_question, answer = generate_similar_questions(question_text)

            Question.objects.create(text=new_question, answer=answer)
            return Response({"text": new_question, "answer": answer})
        
        return Response({"message": "Correct answer recorded"})