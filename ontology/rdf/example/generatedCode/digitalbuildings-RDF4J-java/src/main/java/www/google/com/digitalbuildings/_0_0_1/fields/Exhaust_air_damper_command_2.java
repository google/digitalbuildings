package www.google.com.digitalbuildings._0_0_1.fields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;
import www.google.com.digitalbuildings._0_0_1.subfields.IExhaust;
import www.google.com.digitalbuildings._0_0_1.subfields.Exhaust;
import www.google.com.digitalbuildings._0_0_1.subfields.ICommand;
import www.google.com.digitalbuildings._0_0_1.subfields.Command;
import www.google.com.digitalbuildings._0_0_1.subfields.IAir;
import www.google.com.digitalbuildings._0_0_1.subfields.Air;
import www.google.com.digitalbuildings._0_0_1.subfields.IDamper;
import www.google.com.digitalbuildings._0_0_1.subfields.Damper;


@SuppressWarnings("serial")
public class Exhaust_air_damper_command_2 extends www.google.com.digitalbuildings._0_0_1.fields.Field implements IExhaust_air_damper_command_2{

	IRI newInstance;
	public Exhaust_air_damper_command_2(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/fields#Exhaust_air_damper_command_2"));
	}

	public IRI iri()
	{
		return newInstance;
	}


  public void addComposedOfAir (IAir parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), parameter);
	}

	public Set<IAir> getComposedOfAir (){
		Set<IAir> ComposedOfAir = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), null)
		.objects().forEach(action->{
			if(action instanceof Air) {
				ComposedOfAir.add((Air)action);
			}
		});
		return ComposedOfAir;
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


  public void addComposedOfDamper (IDamper parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), parameter);
	}

	public Set<IDamper> getComposedOfDamper (){
		Set<IDamper> ComposedOfDamper = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), null)
		.objects().forEach(action->{
			if(action instanceof Damper) {
				ComposedOfDamper.add((Damper)action);
			}
		});
		return ComposedOfDamper;
	}


  public void addComposedOfExhaust (IExhaust parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), parameter);
	}

	public Set<IExhaust> getComposedOfExhaust (){
		Set<IExhaust> ComposedOfExhaust = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), null)
		.objects().forEach(action->{
			if(action instanceof Exhaust) {
				ComposedOfExhaust.add((Exhaust)action);
			}
		});
		return ComposedOfExhaust;
	}

	public static Set<IExhaust_air_damper_command_2> getAllExhaust_air_damper_command_2sObjectsCreated(){
		Set<IExhaust_air_damper_command_2> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/fields#Exhaust_air_damper_command_2")).subjects().stream()
		.map(mapper->(IExhaust_air_damper_command_2)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}