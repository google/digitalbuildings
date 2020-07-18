package www.google.com.digitalbuildings._0_0_1.fields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;
import www.google.com.digitalbuildings._0_0_1.subfields.IHigh;
import www.google.com.digitalbuildings._0_0_1.subfields.High;
import www.google.com.digitalbuildings._0_0_1.subfields.ISpeed;
import www.google.com.digitalbuildings._0_0_1.subfields.Speed;
import www.google.com.digitalbuildings._0_0_1.subfields.IFan;
import www.google.com.digitalbuildings._0_0_1.subfields.Fan;
import www.google.com.digitalbuildings._0_0_1.subfields.ICommand;
import www.google.com.digitalbuildings._0_0_1.subfields.Command;
import www.google.com.digitalbuildings._0_0_1.subfields.IDischarge;
import www.google.com.digitalbuildings._0_0_1.subfields.Discharge;


@SuppressWarnings("serial")
public class High_discharge_fan_speed_command extends www.google.com.digitalbuildings._0_0_1.fields.Field implements IHigh_discharge_fan_speed_command{

	IRI newInstance;
	public High_discharge_fan_speed_command(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/fields#High_discharge_fan_speed_command"));
	}

	public IRI iri()
	{
		return newInstance;
	}


  public void addComposedOfCommand (ICommand parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), parameter);
	}

	public Set<ICommand> getComposedOfCommand (){
		Set<ICommand> ComposedOfCommand = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), null)
		.objects().forEach(action->{
			if(action instanceof Command) {
				ComposedOfCommand.add((Command)action);
			}
		});
		return ComposedOfCommand;
	}


  public void addComposedOfDischarge (IDischarge parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), parameter);
	}

	public Set<IDischarge> getComposedOfDischarge (){
		Set<IDischarge> ComposedOfDischarge = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), null)
		.objects().forEach(action->{
			if(action instanceof Discharge) {
				ComposedOfDischarge.add((Discharge)action);
			}
		});
		return ComposedOfDischarge;
	}


  public void addComposedOfFan (IFan parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), parameter);
	}

	public Set<IFan> getComposedOfFan (){
		Set<IFan> ComposedOfFan = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), null)
		.objects().forEach(action->{
			if(action instanceof Fan) {
				ComposedOfFan.add((Fan)action);
			}
		});
		return ComposedOfFan;
	}


  public void addComposedOfHigh (IHigh parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), parameter);
	}

	public Set<IHigh> getComposedOfHigh (){
		Set<IHigh> ComposedOfHigh = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), null)
		.objects().forEach(action->{
			if(action instanceof High) {
				ComposedOfHigh.add((High)action);
			}
		});
		return ComposedOfHigh;
	}


  public void addComposedOfSpeed (ISpeed parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), parameter);
	}

	public Set<ISpeed> getComposedOfSpeed (){
		Set<ISpeed> ComposedOfSpeed = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), null)
		.objects().forEach(action->{
			if(action instanceof Speed) {
				ComposedOfSpeed.add((Speed)action);
			}
		});
		return ComposedOfSpeed;
	}

	public static Set<IHigh_discharge_fan_speed_command> getAllHigh_discharge_fan_speed_commandsObjectsCreated(){
		Set<IHigh_discharge_fan_speed_command> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/fields#High_discharge_fan_speed_command")).subjects().stream()
		.map(mapper->(IHigh_discharge_fan_speed_command)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}