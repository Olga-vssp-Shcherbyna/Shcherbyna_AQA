import pytest


@pytest.mark.api
def test_user_exists(github_api):
    user = github_api.get_user("defunkt")
    assert user["login"] == "defunkt"


@pytest.mark.api
def test_user_not_exists(github_api):
    r = github_api.get_user("butenkosergii")
    assert r["message"] == "Not Found"


@pytest.mark.api
def test_repo_can_be_found(github_api):
    r = github_api.search_repo("become-qa-auto")
    assert r["total_count"] == 42
    assert "become-qa-auto" in r["items"][0]["name"]


@pytest.mark.api
def test_repo_cannot_be_found(github_api):
    r = github_api.search_repo("sergiibutenko_repo_non_exist")
    assert r["total_count"] == 0


@pytest.mark.api
def test_repo_with_singe_char_can_be_found(github_api):
    r = github_api.search_repo("s")
    assert r["total_count"] != 0


@pytest.mark.api
def test_emoji_presence_in_list(github_api):
    r = github_api.list_emoji()
    assert (
        r["polar_bear"]
        == "https://github.githubassets.com/images/icons/emoji/unicode/1f43b-2744.png?v8"
    )


@pytest.mark.api
def test_emoji_non_exist_in_list(github_api):
    r = github_api.list_emoji()
    for item in r:
        assert "good_russian" != item


@pytest.mark.api
def test_commit_author_exists_in_list(github_api):
    r = github_api.get_commits("Olga-vssp-Shcherbyna", "Shcherbyna_AQA")
    assert r[0]["commit"]["author"]["name"] == "Olha Shcherbyna"
