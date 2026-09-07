# Bounded task packets

Use this contract to prepare one independently verifiable outcome for any model. Human-facing examples and installation steps are in the [prompt index](../../prompts/README.md). This document introduces no model provider, automatic delegation, or extra approval flow.

## Inputs

Record a concrete goal, observable acceptance criteria, starting code paths, non-goals, approved decisions, and verification commands or manual evidence. Link the existing plan when continuing work. Discover missing local facts from the repository; ask only for decisions that cannot be inferred safely.

Keep requirements separate from results. An instruction such as `flutter test` is not a passed test. An example budget is not measured performance. A list of starting paths is not a promise that no callers or tests elsewhere are affected.

## Prepare and execute

1. Read AGENTS, PROJECT, current Git state, the active plan, and one relevant prompt or skill.
2. Restate the smallest complete observable result and its constraints. Split unrelated outcomes; retain failure and recovery behavior with the feature that owns them.
3. Identify the existing implementation pattern, actual toolchain, callers, tests, and authoritative references needed for this outcome.
4. Record the baseline, make the change, and run the relevant check. Run broader required checks at integration boundaries, not after every edit.
5. Compare the result with every acceptance criterion. Report untested environments explicitly and leave one concrete next action.

## Optional local generator

After installation, run `python .agents/task_context.py --list` from the app root. Select a task with `--task`, supply `--goal`, one or more `--accept`, and one or more `--check`. Optional `--file`, `--constraint`, and `--plan` provide precise context. Repeat flags for multiple values. The same tool lives at `scripts/task_context.py` in the materials repository.

The generator uses only the Python standard library. It reads the workflow catalog, validates referenced paths, and emits instructions without reading app code, invoking an AI, sending network requests, or executing the supplied checks. It needs repository access when the receiving AI follows the paths. For a chat without file access, explicitly provide the selected documents and sanitized code excerpts.

Output goes to the console. `--output task.md` exclusively creates a UTF-8 file under the selected root in an existing directory. Existing files and paths outside the project are rejected. Do not place secrets in CLI arguments or packets. The tool is intended for a trusted local workspace; it is not a sandbox against concurrent hostile filesystem changes.

## Reusable manual packet

```text
Goal: Restore the approved settings screen's saved preference after restart.
Acceptance: The stored choice is restored; failed writes remain visible and retryable.
Start here: AGENTS.md, PROJECT.md, the active plan, prompts/08-fix-bug.md.
Code scope: Identify the existing settings controller, repository, and regression test.
Constraints: Preserve the approved visual design and existing storage package.
Checks: Reproduce restart and failed writes; run the affected tests and required analysis.
Completion: Report changed paths, observed results, limitations, and the next action in Korean.
```

This is a request example, not an implemented feature or an assertion that those files exist.

## Model handoff and evaluation

Leave the goal, branch and commit, dirty files, accepted decisions, exact failing command, attempted fixes, evidence paths, and next action in the active plan. The receiving model must inspect current files before reusing the result. Keep the same contract when switching models; do not ask the next model to reconstruct the task from an entire conversation.

For a model comparison, use isolated copies of the same starting revision and task inputs. Record completion against criteria, review defects, retries, elapsed time, and billed usage if available. Include at least a maintenance task, an asynchronous failure case, and a document/command consistency task. A successful single example does not establish general quality. No specific model or price tier is certified by this repository.
