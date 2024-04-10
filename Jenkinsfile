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
                    sh 'echo $PATH'
                    sh "/opt/homebrew/bin/kubectl get ns"
                    sh "/opt/homebrew/bin/kubectl apply -f deployment.yaml"
                    sh "sleep 10"
                }
            }
        }
        stage('Pause') {
            steps {
                script {
                    sleep time: 10, unit: 'SECONDS'
                }
            }
        }
        stage('Verification'){
            steps{
                script{
                    sh "/opt/homebrew/bin/kubectl get deployment"
                    sh "/opt/homebrew/bin/kubectl describe deployment shopper-deployment"
                }
            }
        }
    }

}
