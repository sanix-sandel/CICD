pipeline{
    agent any

    stages{

        stage('Deploy to Kubernetes') {
            steps {
                script {
//                     kubernetesDeploy(
//                         configFile: 'deployment.yaml',
//                         kubeconfigId: 'k8s'
//                     )
                    sh 'minikube start'
                    sh "kubectl apply -f deployment.yaml"
                }
            }
        }
    }

}
