output "lambda_function_name" {
  value = aws_lambda_function.sum_lambda.function_name
}

output "api_endpoint" {
  value = aws_apigatewayv2_api.api.api_endpoint
}

output "sns_topic_arn" {
  value = aws_sns_topic.lambda_topic.arn
}
