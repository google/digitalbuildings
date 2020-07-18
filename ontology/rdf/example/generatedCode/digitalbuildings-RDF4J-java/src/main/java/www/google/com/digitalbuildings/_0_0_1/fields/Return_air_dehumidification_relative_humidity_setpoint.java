package www.google.com.digitalbuildings._0_0_1.fields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;
import www.google.com.digitalbuildings._0_0_1.subfields.IRelative;
import www.google.com.digitalbuildings._0_0_1.subfields.Relative;
import www.google.com.digitalbuildings._0_0_1.subfields.IReturn;
import www.google.com.digitalbuildings._0_0_1.subfields.Return;
import www.google.com.digitalbuildings._0_0_1.subfields.IDehumidification;
import www.google.com.digitalbuildings._0_0_1.subfields.Dehumidification;
import www.google.com.digitalbuildings._0_0_1.subfields.IHumidity;
import www.google.com.digitalbuildings._0_0_1.subfields.Humidity;
import www.google.com.digitalbuildings._0_0_1.subfields.ISetpoint;
import www.google.com.digitalbuildings._0_0_1.subfields.Setpoint;
import www.google.com.digitalbuildings._0_0_1.subfields.IAir;
import www.google.com.digitalbuildings._0_0_1.subfields.Air;


@SuppressWarnings("serial")
public class Return_air_dehumidification_relative_humidity_setpoint extends www.google.com.digitalbuildings._0_0_1.fields.Field implements IReturn_air_dehumidification_relative_humidity_setpoint{

	IRI newInstance;
	public Return_air_dehumidification_relative_humidity_setpoint(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/fields#Return_air_dehumidification_relative_humidity_setpoint"));
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


  public void addComposedOfDehumidification (IDehumidification parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), parameter);
	}

	public Set<IDehumidification> getComposedOfDehumidification (){
		Set<IDehumidification> ComposedOfDehumidification = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), null)
		.objects().forEach(action->{
			if(action instanceof Dehumidification) {
				ComposedOfDehumidification.add((Dehumidification)action);
			}
		});
		return ComposedOfDehumidification;
	}


  public void addComposedOfHumidity (IHumidity parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), parameter);
	}

	public Set<IHumidity> getComposedOfHumidity (){
		Set<IHumidity> ComposedOfHumidity = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), null)
		.objects().forEach(action->{
			if(action instanceof Humidity) {
				ComposedOfHumidity.add((Humidity)action);
			}
		});
		return ComposedOfHumidity;
	}


  public void addComposedOfRelative (IRelative parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), parameter);
	}

	public Set<IRelative> getComposedOfRelative (){
		Set<IRelative> ComposedOfRelative = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), null)
		.objects().forEach(action->{
			if(action instanceof Relative) {
				ComposedOfRelative.add((Relative)action);
			}
		});
		return ComposedOfRelative;
	}


  public void addComposedOfReturn (IReturn parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), parameter);
	}

	public Set<IReturn> getComposedOfReturn (){
		Set<IReturn> ComposedOfReturn = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), null)
		.objects().forEach(action->{
			if(action instanceof Return) {
				ComposedOfReturn.add((Return)action);
			}
		});
		return ComposedOfReturn;
	}


  public void addComposedOfSetpoint (ISetpoint parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), parameter);
	}

	public Set<ISetpoint> getComposedOfSetpoint (){
		Set<ISetpoint> ComposedOfSetpoint = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), null)
		.objects().forEach(action->{
			if(action instanceof Setpoint) {
				ComposedOfSetpoint.add((Setpoint)action);
			}
		});
		return ComposedOfSetpoint;
	}

	public static Set<IReturn_air_dehumidification_relative_humidity_setpoint> getAllReturn_air_dehumidification_relative_humidity_setpointsObjectsCreated(){
		Set<IReturn_air_dehumidification_relative_humidity_setpoint> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/fields#Return_air_dehumidification_relative_humidity_setpoint")).subjects().stream()
		.map(mapper->(IReturn_air_dehumidification_relative_humidity_setpoint)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}