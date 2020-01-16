import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import make_regression
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.model_selection import learning_curve

_, axes = plt.subplots(2, 3, figsize=(20, 5))


def render_learning_curve(train_sizes, train_scores, test_scores, fit_times, subplot_index):
    axes[subplot_index, 0].set_title('Learning curve')

    train_scores_mean = np.mean(train_scores, axis=1)
    train_scores_std = np.std(train_scores, axis=1)
    test_scores_mean = np.mean(test_scores, axis=1)
    test_scores_std = np.std(test_scores, axis=1)
    fit_times_mean = np.mean(fit_times, axis=1)
    fit_times_std = np.std(fit_times, axis=1)

    # Plot learning curve
    axes[subplot_index, 0].grid()
    axes[subplot_index, 0].fill_between(train_sizes, train_scores_mean - train_scores_std,
                                        train_scores_mean + train_scores_std, alpha=0.1,
                                        color="r")
    axes[subplot_index, 0].fill_between(train_sizes, test_scores_mean - test_scores_std,
                                        test_scores_mean + test_scores_std, alpha=0.1,
                                        color="g")
    axes[subplot_index, 0].plot(train_sizes, train_scores_mean, 'o-', color="r",
                                label="Training score")
    axes[subplot_index, 0].plot(train_sizes, test_scores_mean, 'o-', color="g",
                                label="Cross-validation score")
    axes[subplot_index, 0].legend(loc="best")

    # Plot n_samples vs fit_times
    axes[subplot_index, 1].grid()
    axes[subplot_index, 1].plot(train_sizes, fit_times_mean, 'o-')
    axes[subplot_index, 1].fill_between(train_sizes, fit_times_mean - fit_times_std,
                                        fit_times_mean + fit_times_std, alpha=0.1)
    axes[subplot_index, 1].set_xlabel("Training examples")
    axes[subplot_index, 1].set_ylabel("fit_times")
    axes[subplot_index, 1].set_title("Scalability of the model")

    # Plot fit_time vs score
    axes[subplot_index, 2].grid()
    axes[subplot_index, 2].plot(fit_times_mean, test_scores_mean, 'o-')
    axes[subplot_index, 2].fill_between(fit_times_mean, test_scores_mean - test_scores_std,
                                        test_scores_mean + test_scores_std, alpha=0.1)
    axes[subplot_index, 2].set_xlabel("fit_times")
    axes[subplot_index, 2].set_ylabel("Score")
    axes[subplot_index, 2].set_title("Performance of the model")


if __name__ == '__main__':
    x, y = make_regression(random_state=42)
    train_sizes, train_scores, test_scores, fit_times, _ = learning_curve(LinearRegression(), x, y, cv=7,
                                                                          n_jobs=5, return_times=True)
    render_learning_curve(train_sizes, train_scores, test_scores, fit_times, 0)

    x, y = make_regression(random_state=42)
    x = x * 10
    x = x.astype(int)
    y = y * 10
    y = y.astype(int)
    train_sizes, train_scores, test_scores, fit_times, _ = learning_curve(LogisticRegression(), x, y, cv=2,
                                                                          n_jobs=2, return_times=True, verbose=3)
    render_learning_curve(train_sizes, train_scores, test_scores, fit_times, 1)

    plt.show()
    exit()
