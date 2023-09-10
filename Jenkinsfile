pipeline {
  agent any
  stages {
    stage('version') {
      steps {
        sh 'python --version'
      }
    }
    stage('install requirements.txt') {
      steps {
        sh 'pip install -r requirements.txt'
      }
    }
    stage('run hello') {
      steps {
        sh 'python hello.py'
      }
    }
  }
}