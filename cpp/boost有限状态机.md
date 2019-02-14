# 如何使用boost的MSM

## 最简单的

```cpp
#include <boost/msm/front/euml/euml.hpp>
#include <boost/msm/front/euml/state_grammar.hpp>
#include <boost/msm/back/state_machine.hpp>
#include <iostream>

namespace msm = boost::msm;
using namespace boost::msm::front::euml;

BOOST_MSM_EUML_STATE((), Off)
BOOST_MSM_EUML_STATE((), On)

BOOST_MSM_EUML_EVENT(press)

BOOST_MSM_EUML_TRANSITION_TABLE((
  Off + press == On,
  On + press == Off
), light_transition_table)

BOOST_MSM_EUML_DECLARE_STATE_MACHINE(
(light_transition_table, init_ << Off),
light_state_machine)

int main()
{
  msm::back::state_machine<light_state_machine> light;
  std::cout << *light.current_state() << '\n';
  light.process_event(press);
  std::cout << *light.current_state() << '\n';
  light.process_event(press);
  std::cout << *light.current_state() << '\n';
}
```

  按一下换一个状态

## 状态变化触发函数

```cpp
#include <boost/msm/front/euml/euml.hpp>
#include <boost/msm/front/euml/state_grammar.hpp>
#include <boost/msm/back/state_machine.hpp>
#include <iostream>

namespace msm = boost::msm;
using namespace boost::msm::front::euml;

BOOST_MSM_EUML_STATE((), Off)
BOOST_MSM_EUML_STATE((), On)

BOOST_MSM_EUML_EVENT(press)

BOOST_MSM_EUML_ACTION(switch_light)
{
  template <class Event, class Fsm>
  void operator()(const Event &ev, Fsm &fsm,
    BOOST_MSM_EUML_STATE_NAME(Off) &sourceState,
    BOOST_MSM_EUML_STATE_NAME(On) &targetState) const
  {
    std::cout << "Switching on\n";
  }

  template <class Event, class Fsm>
  void operator()(const Event &ev, Fsm &fsm,
    decltype(On) &sourceState,
    decltype(Off) &targetState) const
  {
    std::cout << "Switching off\n";
  }
};

BOOST_MSM_EUML_TRANSITION_TABLE((
  Off + press / switch_light == On,
  On + press / switch_light == Off
), light_transition_table)

BOOST_MSM_EUML_DECLARE_STATE_MACHINE(
(light_transition_table, init_ << Off),
light_state_machine)

int main()
{
  msm::back::state_machine<light_state_machine> light;
  light.process_event(press);
  light.process_event(press);
}
```

触发状态变化的函数，action写在event后，加个`/`

## 加一个变化状态

```cpp
#include <boost/msm/front/euml/euml.hpp>
#include <boost/msm/front/euml/state_grammar.hpp>
#include <boost/msm/back/state_machine.hpp>
#include <iostream>

namespace msm = boost::msm;
using namespace boost::msm::front::euml;

BOOST_MSM_EUML_STATE((), Off)
BOOST_MSM_EUML_STATE((), On)

BOOST_MSM_EUML_EVENT(press)

BOOST_MSM_EUML_ACTION(is_broken)
{
  template <class Event, class Fsm, class Source, class Target>
  bool operator()(const Event &ev, Fsm &fsm, Source &src, Target &trg) const
  {
    return true;
  }
};

BOOST_MSM_EUML_ACTION(switch_light)
{
  template <class Event, class Fsm, class Source, class Target>
  void operator()(const Event &ev, Fsm &fsm, Source &src, Target &trg) const
  {
    std::cout << "Switching\n";
  }
};

BOOST_MSM_EUML_TRANSITION_TABLE((
  Off + press [!is_broken] / switch_light == On,
  On + press / switch_light == Off
), light_transition_table)

BOOST_MSM_EUML_DECLARE_STATE_MACHINE(
(light_transition_table, init_ << Off),
light_state_machine)

int main()
{
  msm::back::state_machine<light_state_machine> light;
  light.process_event(press);
  light.process_event(press);
}

```

## 进入某种状态，退出某种状态

```cpp
#include <boost/msm/front/euml/euml.hpp>
#include <boost/msm/front/euml/state_grammar.hpp>
#include <boost/msm/back/state_machine.hpp>
#include <iostream>

namespace msm = boost::msm;
using namespace boost::msm::front::euml;

BOOST_MSM_EUML_ACTION(state_entry)
{
  template <class Event, class Fsm, class State>
  void operator()(const Event &ev, Fsm &fsm, State &state) const
  {
    std::cout << "Entering\n";
  }
};

BOOST_MSM_EUML_ACTION(state_exit)
{
  template <class Event, class Fsm, class State>
  void operator()(const Event &ev, Fsm &fsm, State &state) const
  {
    std::cout << "Exiting\n";
  }
};

BOOST_MSM_EUML_STATE((state_entry, state_exit), Off)
BOOST_MSM_EUML_STATE((state_entry, state_exit), On)

BOOST_MSM_EUML_EVENT(press)

BOOST_MSM_EUML_TRANSITION_TABLE((
  Off + press == On,
  On + press == Off
), light_transition_table)

BOOST_MSM_EUML_DECLARE_STATE_MACHINE(
(light_transition_table, init_ << Off),
light_state_machine)

int main()
{
  msm::back::state_machine<light_state_machine> light;
  light.process_event(press);
  light.process_event(press);
}
```

## 带变量

```cpp
#include <boost/msm/front/euml/euml.hpp>
#include <boost/msm/front/euml/state_grammar.hpp>
#include <boost/msm/back/state_machine.hpp>
#include <iostream>

namespace msm = boost::msm;
using namespace boost::msm::front::euml;

BOOST_MSM_EUML_DECLARE_ATTRIBUTE(int, switched_on)

BOOST_MSM_EUML_ACTION(state_entry)
{
  template <class Event, class Fsm, class State>
  void operator()(const Event &ev, Fsm &fsm, State &state) const
  {
    std::cout << "Switched on\n";
    ++fsm.get_attribute(switched_on);
  }
};
BOOST_MSM_EUML_ACTION(is_broken)
{
  template <class Event, class Fsm, class Source, class Target>
  bool operator()(const Event &ev, Fsm &fsm, Source &src, Target &trg) const
  {
    return fsm.get_attribute(switched_on) > 1;
  }
};

BOOST_MSM_EUML_STATE((), Off)
BOOST_MSM_EUML_STATE((state_entry), On)
BOOST_MSM_EUML_EVENT(press)

BOOST_MSM_EUML_TRANSITION_TABLE((
  Off + press [!is_broken] == On,
  On + press == Off
), light_transition_table)

BOOST_MSM_EUML_DECLARE_STATE_MACHINE(
(light_transition_table, init_ << Off, no_action, no_action,
attributes_ << switched_on), light_state_machine)

int main()
{
  msm::back::state_machine<light_state_machine> light;
  light.process_event(press);
  light.process_event(press);
  light.process_event(press);
  light.process_event(press);
  light.process_event(press);
}
```

## 在表里用attribute

```cpp
#include <boost/msm/front/euml/euml.hpp>
#include <boost/msm/front/euml/state_grammar.hpp>
#include <boost/msm/back/state_machine.hpp>
#include <iostream>

namespace msm = boost::msm;
using namespace boost::msm::front::euml;

BOOST_MSM_EUML_DECLARE_ATTRIBUTE(int, switched_on)

void write_message()
{
  std::cout << "Switched on\n";
}

BOOST_MSM_EUML_FUNCTION(WriteMessage_, write_message, write_message_,
  void, void)

BOOST_MSM_EUML_STATE((), Off)
BOOST_MSM_EUML_STATE((), On)

BOOST_MSM_EUML_EVENT(press)

BOOST_MSM_EUML_TRANSITION_TABLE((
  Off + press [fsm_(switched_on) < Int_<2>()] / (++fsm_(switched_on),
    write_message_()) == On,
  On + press == Off
), light_transition_table)

BOOST_MSM_EUML_DECLARE_STATE_MACHINE(
(light_transition_table, init_ << Off, no_action, no_action,
attributes_ << switched_on), light_state_machine)

int main()
{
  msm::back::state_machine<light_state_machine> light;
  light.process_event(press);
  light.process_event(press);
  light.process_event(press);
  light.process_event(press);
  light.process_event(press);
}
```

