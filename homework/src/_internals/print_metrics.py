def print_metrics(title, mse, mae, r2):
    print()
    print(title, ":", sep="")
    print()
    print("Metricas de entrenamiento:")
    print(f"  MSE: {mse}")
    print(f"  MAE: {mae}")
    print(f"  R2: {r2}")
