"""
API Serializers
"""
from rest_framework import serializers

from lms.djangoapps.program_enrollments.models import ProgramEnrollment

class ProgramEnrollmentSerializer(serializers.ModelSerializer):
    """
    Serializer for Program Enrollments
    """
    
    class Meta(object):
        model = ProgramEnrollment
        fields = ('user', 'external_user_key', 'program_uuid', 'curriculum_uuid', 'status')
